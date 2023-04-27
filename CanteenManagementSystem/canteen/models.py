from django.db import models

# Create your models here.
class Contact_Message(models.Model):
    C_Id    = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=30)
    mail    = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timeofM = models.DateTimeField(auto_now_add=True, blank= True)

    def __str__(self):
        return self.name

class User_register(models.Model):
    C_Id    = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=30)
    mail    = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timeofM = models.DateTimeField(auto_now_add=True, blank= True)

    def __str__(self):
        return self.name  

    #product table
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='ResturantImage', default="")

    def __str__(self):
        return self.product_name  
    
