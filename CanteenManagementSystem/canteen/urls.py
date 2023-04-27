from django.contrib import admin
from django.urls import path
from canteen import views

urlpatterns = [
   path("", views.index, name='home') ,
   path("contact", views.contact, name='contact'),
   path("signup", views.signup, name='signup'),
   path("login", views.loginCanteen, name='login'),
   path("logout", views.logoutCanteen, name='logout'),
   path('menu/', views.menu_view, name='menu'),
   path('checkout', views.checkout, name='checkout'),
      
]
