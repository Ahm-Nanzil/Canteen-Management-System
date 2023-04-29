from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from canteen.models import Contact_Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from . models import Product
from . models import Order
from . models import Subscriber
import json
import datetime


# Create your views here.
# def index(request):
#     products= Product.objects.all()
#     n= len(products)
#     orders = Order.objects.filter(user=request.user)
#     if request.user.is_authenticated:
#         params={'product_list': products, 'order_list':orders} 
#         return render(request,"index.html",params)
#     else:
#         params={'product_list': products} 
#         return render(request,"index.html",params)
def index(request):
    products = Product.objects.all()
    n = len(products)
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        params = {'product_list': products, 'order_list': orders} 
    else:
        params = {'product_list': products} 
    return render(request, "index.html", params)

    

def contact(request):
    if request.method == 'POST':
        messages.success(request, "Message sent Sucessfully")
        name = request.POST['name']
        mail = request.POST['mail']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_m=Contact_Message(name=name,mail=mail,subject=subject,message=message)
        contact_m.save()
        response_data = {'success': True, 'message': 'Your message has been sent. Thank you!'}
        return JsonResponse(response_data)
    else:
        response_data = {'error': True, 'message': 'Message sent fail.'}
        return JsonResponse(response_data)

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        phone= request.POST['phone']
        password = request.POST['password']
        
        canteenUser = User.objects.create_user(name,mail,password)
        canteenUser.phone = phone
        canteenUser.save()
        
        response_data = {'success': True, 'message': 'User registered successfully!'}
        return JsonResponse(response_data)

    else:
        response_data = {'error': True, 'message': 'Signup failed. Please try again.'}
        return JsonResponse(response_data)

def loginCanteen(request):
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



def menu_view(request):
    print("The URL '/menu/' has been accessed!")
    menu_items = Product.objects.all()
    print(menu_items)

    # Render the menu page with the retrieved menu items
    return render(request, 'menu.html', {'menu_items': menu_items})


import datetime


def checkout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cart_data = request.POST.get('cartData')
            if cart_data:
                cart = json.loads(cart_data)
                user_id = request.user.id
                user = User.objects.get(pk=user_id)
                total_price = 0
                current_time = datetime.datetime.now() # set current date and time
                for item_id, item in cart.items():
                    product_id = int(item_id)
                    product = Product.objects.get(pk=product_id)
                    product_price = product.price
                    product_name = item['name']
                    product_image = item['image']
                    quantity = item['quantity']
                    # address = request.POST.get('address')
                    address = "Mirpur"
                    total_price =product_price * quantity
                    order = Order(user=user, product=product, quantity=quantity, total_price=total_price,address=address, order_date=current_time) # add current_time to order
                    order.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid cart data'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request method'})

    else:
            return JsonResponse({'success': False, 'error': 'Invalid request method'})

def profile(request):
    
    return render(request,"profile.html")

def userprofile(request):
    
    return render(request,"profile.html")


def subscribe(request):
    if request.method == 'POST':
        # messages.success(request, "Message sent Sucessfully")
        
        mail = request.POST['email']
        current_time = datetime.datetime.now()
        new_subscriber=Subscriber(mail=mail,subscribe_date=current_time)
        
        new_subscriber.save()
        response_data = {'success': True, 'message': 'Your message has been sent. Thank you!'}
        return JsonResponse(response_data)
    else:
        response_data = {'error': True, 'message': 'Message sent fail.'}
        return JsonResponse(response_data)