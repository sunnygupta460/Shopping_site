from django.contrib import admin
#from django.contrib import admin as django_admin
from import_export.admin import ImportExportModelAdmin
from .models import Order

admin.site.register(Order)

class OrderAdmin(ImportExportModelAdmin):
    list_display = ['orderdate','quantity','orderstatus']
    search_fields = ['orderdate']
