from django.db import models
import datetime

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_last_date = models.DateField()
    product_description = models.TextField()
    product_price = models.PositiveSmallIntegerField()

class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name
    
class Product_2(models.Model):
    product_name_2 = models.CharField(max_length=255)
    product_last_date_2 = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=7))
    product_description_2 = models.TextField(null=False, blank=False)
    product_price_2 = models.PositiveSmallIntegerField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product_2'
        verbose_name_plural = 'Products_2'

    def __str__(self) -> str:
        return self.product_name_2
    
    
class Busket(models.Model):
    size_busket = models.CharField(max_length=100)
    weight_busket = models.PositiveSmallIntegerField(null=True, blank=True)
    capacity_busket = models.PositiveSmallIntegerField(null=True, blank=True)
    products_in_busket = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self) -> str:
        return self.size_busket
