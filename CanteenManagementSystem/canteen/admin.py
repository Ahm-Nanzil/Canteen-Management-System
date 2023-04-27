from django.contrib import admin
from .models import Contact_Message
from .models import User_register
from .models import Product

# Register your models here.
admin.site.register(Contact_Message)
admin.site.register(User_register)
admin.site.register(Product)
