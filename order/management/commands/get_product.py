import mws
from django.core.management.base import BaseCommand
from shopping.settings import MWS_ACCESS_KEY, MWS_ACCOUNT_ID, MWS_SECRET_KEY


class Command(BaseCommand):

	def handle(self, *args, **options):
		product_api = mws.Products(
			access_key=MWS_ACCESS_KEY,
			secret_key=MWS_SECRET_KEY,
			account_id=MWS_ACCOUNT_ID,
			region='IN',
		)
		service_status = product_api.get_service_status()
		# products = product_api.list_matching_products(marketplaceid="A21TJRUUN4KGV", query="book")
		print(product_api.auth_token, product_api.domain)
