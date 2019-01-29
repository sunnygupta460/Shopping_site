
from django.contrib import admin
#from django.contrib import admin as django_admin
from import_export.admin import ImportExportModelAdmin

from .models import Product, Purchase

@admin.register(Product)


class ProductAdmin(ImportExportModelAdmin):

    
    list_display = ['name', 'price', 'store', 'sale_price', 'stock']
    search_fields=('name',)

admin.site.register(Purchase)

class PurchaseAdmin(ImportExportModelAdmin):

    list_display = ['quantity','orderdate','amountpaid']
    search_fields=('quantity',)