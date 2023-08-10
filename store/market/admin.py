from django.contrib import admin
from .models import Product, Busket, Product_2

# Register your models here.
admin.site.register(Product)


@admin.register(Product_2)
class Product_2Admin(admin.ModelAdmin):
    list_display = ('product_name_2','product_last_date_2','product_description_2','product_price_2')

@admin.register(Busket)
class BusketAdmin(admin.ModelAdmin):
    list_display = ('size_busket','weight_busket','capacity_busket')