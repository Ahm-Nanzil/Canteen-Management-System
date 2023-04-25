from django.contrib import admin
from django.urls import path
from canteen import views

urlpatterns = [
   path("", views.index, name='home') ,
   path("login", views.login, name='login'),
   path("contact", views.contact, name='contact'),
   path("/hello", views.hello, name='hello'),
   path("signup", views.signup, name='signup'),
   path("login", views.login, name='login'),
   path("logout", views.logoutCanteen, name='logout'),
      
]
