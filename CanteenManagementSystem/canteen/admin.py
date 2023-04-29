from django.contrib import admin
from .models import Contact_Message
from .models import User_register
from .models import Product
from .models import Order
from .models import Subscriber

# Register your models here.
admin.site.register(Contact_Message)
admin.site.register(User_register)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Subscriber)

