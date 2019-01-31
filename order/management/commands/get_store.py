from django.core.management.base import BaseCommand
import mws, os
from store.models import Store
from shopping import settings

class Command(BaseCommand):

	def handle(self, *args, **options):
		store_api = mws.Stores(
			access_key=settings.MWS_ACCESS_KEY,
			secret_key=settings.MWS_SECRET_KEY,
			account_id=settings.MWS_ACCOUNT_ID,
			region='IN',
			)
		
		service_status = store_api.get_service_status()
		service_status
		service_status.original
		service_status.parsed
		service_status.response

		# Create the entry in the store model