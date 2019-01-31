from django.core.management.base import BaseCommand
import mws, os
from order.models import Order
from shopping import settings
class Command(BaseCommand):

	def handle(self, *args, **options):

		order_api = mws.Orders(
			access_key=settings.MWS_ACCESS_KEY,
			secret_key=settings.MWS_SECRET_KEY,
			account_id=settings.MWS_ACCOUNT_ID,
			region='IN',
			)
		
		service_status = order_api.get_service_status()
		service_status
		service_status.original
		service_status.parsed
		service_status.response
		print(service_status.parsed)
		# Create the entry in the order model
		# Order.objects.create()