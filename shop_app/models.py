from django.db import models
from random import randint
from auth_app.models import User


class Category(models.Model):
    name=models.CharField(max_length=40,null=False,blank=False)

    def __str__(self):
         return self.name

class Tag(models.Model):
    name=models.CharField(max_length=40,null=False,blank=False)

    def __str__(self):
         return self.name


class Product(models.Model):
    name=models.CharField(max_length=80,null=False,blank=False)
    product_image= models.ImageField(upload_to='product_image/',null=False,blank=False)
    price = models.PositiveIntegerField()
    short_description=models.TextField(max_length=800,null=False,blank=False)
    long_description=models.TextField(max_length=1000,null=False,blank=False)
    category=models.ManyToManyField(Category,blank=True)
    tags = models.ManyToManyField(Tag,blank=True)
    is_featured =models.BooleanField(default=False)

    def get_product_code(self):
        return randint(101,999)

    def __str__(self):
        return self.name

class Cart(models.Model):
    owner = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.owner)
    
    # Creating Model Property to calculate Quantity x Price
    @property
    def total_price(self):
        return self.quantity * self.product.price

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled')
)

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    address=models.CharField(max_length=180,null=False,blank=False)
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="Ordered Date")
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default="Pending"
        )


