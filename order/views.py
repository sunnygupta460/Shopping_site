from order.models import Order, Marketplace
from rest_framework import viewsets
from order.serializers import OrderSerializer, MarketplaceSerializer



class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	class MarketplaceViewSet(viewsets.ModelViewSet):
		queryset = Marketplace.objects.all()
		serializers_class = MarketplaceSerializer