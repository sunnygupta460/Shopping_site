from django.contrib import admin
from django.contrib import admin as django_admin
from import_export.admin import ImportExportModelAdmin
from .models import Store, Storefees
from .models import *


admin.site.register(Store)

class StoreAdmin(ImportExportModelAdmin):

	list_display = ['name','user','api_key','user_key','store_key']
	search_fields=('name',)

admin.site.register(Storefees)

class StorefeesAdmin(ImportExportModelAdmin):

	list_display = ['store_id','store_type','description','amount']
	search_fields=('store_type',)
	