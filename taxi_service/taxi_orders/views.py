from .models import Order
from django.shortcuts import render

def index(request):
    orders = Order.objects.all()
    return render(request, "taxi_orders/index.html", {'orders': orders})
