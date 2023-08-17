from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    best_before_date = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=7))
    description = models.TextField(null=False, blank=False)
    price = models.PositiveSmallIntegerField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return self.name
       

class Busket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    

