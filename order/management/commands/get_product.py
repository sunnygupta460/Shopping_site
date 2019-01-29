from django.core.management.base import BaseCommand
import mws, os
from product.models import Product

class Command(BaseCommand):

	def handle(self, *args, **options):
		product_api = mws.Products(
			access_key=os.environ['MWS_ACCESS_KEY'],
			secret_key=os.environ['MWS_SECRET_KEY'],
			account_id=os.environ['MWS_ACCOUNT_ID'],
			region='IN',
			)
		
		service_status = product_api.get_service_status()
		service_status
		service_status.original
		service_status.parsed
		service_status.response

		# Create the entry in the product model