
from rest_framework import serializers
from product.models import Product, Purchase

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields =('name','price','store','active')


class PurchaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Purchase
		fields =('quantity','orderdate','amountpaid')