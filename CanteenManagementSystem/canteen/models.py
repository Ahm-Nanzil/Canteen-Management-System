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
    
