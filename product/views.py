from product.models import Product, Purchase
from rest_framework import viewsets
from product.serializers import ProductSerializer, PurchaseSerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer


