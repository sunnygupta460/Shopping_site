
from rest_framework import serializers
from store.models import Store, Storefees

class StoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Store
		fields =('name','api_key','user_key','store_key')


class StorefeesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Storefees
		fields =('store','store_type','description','amountpaid')