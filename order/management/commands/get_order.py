from django.core.management.base import BaseCommand
import mws, os
from order.models import Order

class Command(BaseCommand):

	def handle(self, *args, **options):

		orders_api = mws.Orders(
			access_key=os.environ['MWS_ACCESS_KEY'],
			secret_key=os.environ['MWS_SECRET_KEY'],
			account_id=os.environ['MWS_ACCOUNT_ID'],
			region='IN',
			)
		
		service_status = orders_api.get_service_status()
		service_status
		service_status.original
		service_status.parsed
		service_status.response

		# Create the entry in the order model
		Orders.objects.create()