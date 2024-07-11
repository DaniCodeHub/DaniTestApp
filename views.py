from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import Broker
from .models import Seller

# Create your views here.
def home(request):
    return render(request, "home.html")
    #return HttpResponse("Hello World")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def broker(request):
    name = Broker.objects.all()
    return render(request, "broker.html", {"broker": name})

def seller(request):
    seller_name = Seller.objects.all()
    return render(request, "seller.html", {"seller_list": seller_name})