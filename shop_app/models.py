from django.db import models


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
        return f'AE-{223}'

    def __str__(self):
        return self.name


