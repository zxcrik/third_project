from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Busket, Category 
from .forms import *


# Create your views here.


menu = [
    {'title':'Home','url':'home'},
    {'title':'List of products','url':'products'},
    {'title':'Your busket','url':'busket'},
]


def Home(request):
    data = {
        'title':'Главная',
        'menu':menu,   
    }
    return render(request, 'market/Home.html', data)

def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    data = {
        'title':'Список продуктов',
        'menu':menu,
        'products':products,
        'categories':categories
    }
    return render(request,'market/products.html', data)

def busket(request):
    busket_items = Product.objects.all()
    data = {
        'title':'Корзина с продуктами',
        'menu':menu,
        'busket_items':busket_items,
    }
    return render(request, 'market/busket.html', data)

def desc(request, product_id):
    product = Product.objects.get(id=product_id)

    data = {
        'title':'Описание продуктов',
        'menu':menu,
        'product':product,
    }
    return render(request, 'market/desc.html', data)

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Product.objects.create(**form_data)
            redirect('products')
    else:
        form = AddProductForm()

    data = {
        'menu': menu,
        'title': 'Добавить новый продукт',
        'form': form    
    }
    return render(request, 'market/add-product.html', data)