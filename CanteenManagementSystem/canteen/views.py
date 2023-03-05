from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

#it is login view
def login(request):
    return render(request, "login.html")