from django.shortcuts import render

from .models import Order

def home_function(request):
    # some logic here
    return render(request, 'index.html')

def delivery_function(request):
    return render(request, 'delivery_msg.html')

def items_function(request):
    return render(request, 'items.html')


def popcorn_order(request):
    if request.method == "POST":
        order = Order()
        
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        adress = request.POST.get('adress')
        store_name = request.POST.get('store_name')
        quantity = request.POST.get('quantity')
    
        order.name = name
        order.phone = phone
        order.adress = adress
        order.store_name = store_name
        order.quantity = quantity
    
        order.save()
       
        return render(request, 'delivery_msg.html')
    else : return render(request, 'popcorn_order.html')

 
