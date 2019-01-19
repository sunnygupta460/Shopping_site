
from django.contrib import admin
from django.contrib import admin as django_admin

from .models import Product, Purchase

class ProductAdmin(django_admin.ModelAdmin):
    list_display = ['name', 'price', 'store', 'sale_price', 'stock']
    list_filters = ['price']
    search_fields = ['name']
admin.site.register(Product, ProductAdmin)

class PurchaseAdmin(django_admin.ModelAdmin):
    list_display = ['quantity','orderdate','amountpaid']
    list_filters = ['orderdate']
    search_fields = ['quantity']
admin.site.register(Purchase, PurchaseAdmin)
