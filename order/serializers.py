from rest_framework import serializers
from order.models import Order, Marketplace

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields =('pro_id','orderdate','quantity','orderstatus')

class MarketplaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Marketplace
		fields =('name','conn_method')