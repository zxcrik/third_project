from django.shortcuts import render
from django.http import HttpResponse
from .models import Product_2, Busket, Category


# Create your views here.


menu = [
    {'title':'Home','url':'home'},
    {'title':'List of products','url':'products'},
    {'title':'Your busket','url':'busket'}
]



def Home(request):
    data = {
        'title':'Главная',
        'menu':menu,   
    }
    return render(request, 'market/Home.html', data)

def products(request):
    products = Product_2.objects.all()
    categories = Category.objects.all()
    data = {
        'title':'Список продуктов',
        'menu':menu,
        'products':products,
        'categories':categories
    }
    return render(request,'market/products.html', data)

def busket(request):
    busket_items = Busket.objects.all()
    data = {
        'title':'Корзина с продуктами',
        'menu':menu,
        'busket_items':busket_items
    }
    return render(request, 'market/busket.html', data)


