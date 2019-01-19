from django.contrib import admin
from django.contrib import admin as django_admin
from .models import Store

class StoreAdmin(django_admin.ModelAdmin):
    list_display = ['name', 'address', 'mobile']
    list_filters = ['name']
    search_fields = ['name']
admin.site.register(Store, StoreAdmin)
