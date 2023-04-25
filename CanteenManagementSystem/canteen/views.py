from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from canteen.models import Contact_Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "index.html")


def contact(request):
    messages.success(request, "Message sent Sucessfully")
    name = request.POST['name']
    mail = request.POST['mail']
    subject = request.POST['subject']
    message = request.POST['message']
    contact_m=Contact_Message(name=name,mail=mail,subject=subject,message=message)
    contact_m.save()
    return render(request, "index.html")

def hello(request):
    messages.success(request, "Welcome to login")
    return render(request, "hello.html")

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        phone= request.POST['phone']
        password = request.POST['password']
        
        canteenUser = User.objects.create_user(name,mail,password)
        canteenUser.phone = phone
        canteenUser.save()
        return redirect('/')


    else:
        return HttpResponse('Not found')   

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        print(name)
        user= authenticate(username=name,password=password)
        if user is not None:
            messages.success(request, "Login")
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, "Worng")
            return redirect('/')


    else:
        return HttpResponse('Not found')  


def logoutCanteen(request):
    logout(request)
    return redirect('/')