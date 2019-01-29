from django.core.management.base import BaseCommand
import mws, os
from store.models import Store

class Command(BaseCommand):

	def handle(self, *args, **options):

		order_api = mws.Store(
			access_key=os.environ['MWS_ACCESS_KEY'],
			secret_key=os.environ['MWS_SECRET_KEY'],
			account_id=os.environ['MWS_ACCOUNT_ID'],
			region='IN',
			)
		
		service_status = store_api.get_service_status()
		service_status
		service_status.original
		service_status.parsed
		service_status.response