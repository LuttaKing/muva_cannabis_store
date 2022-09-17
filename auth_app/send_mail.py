
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generate_token
import threading

class EmailThread(threading.Thread):

    def __init__(self,email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_activation_email(user,request):
    current_site = get_current_site(request)
    email_subject = "Activate account"
    email_body = render_to_string('authentication/activate.html', {
        'user':user,
        'domain':current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':generate_token.make_token(user),
    })

    email=EmailMessage(subject=email_subject,body=email_body,from_email=settings.EMAIL_FROM_USER,to=[user.email])
    # email.send() no thread, use next
    EmailThread(email).start()