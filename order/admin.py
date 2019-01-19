

from django.contrib import admin
from django.contrib import admin as django_admin
from .models import Order

class OrderAdmin(django_admin.ModelAdmin):
    list_display = ['orderdate','quantity','orderstatus']
    list_filters = ['orderdate']
    search_fields = ['orderdate']
admin.site.register(Order, OrderAdmin)
