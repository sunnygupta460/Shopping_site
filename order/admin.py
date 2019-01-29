from django.contrib import admin
#from django.contrib import admin as django_admin
from import_export.admin import ImportExportModelAdmin
from .models import Order, Marketplace

admin.site.register(Order)

class OrderAdmin(ImportExportModelAdmin):
    list_display = ['orderdate','quantity','orderstatus']
    search_fields = ['orderdate']

admin.site.register(Marketplace)

class MarketplaceAdmin(ImportExportModelAdmin):
    list_display = ['name','conn_method']
    search_fields = ['name']
