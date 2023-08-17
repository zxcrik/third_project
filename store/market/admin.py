from django.contrib import admin
from .models import Product, Busket, Category

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','description','price', 'category')
    
@admin.register(Busket)    
class BusketAdmin(admin.ModelAdmin):
    list_display = ('product',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


