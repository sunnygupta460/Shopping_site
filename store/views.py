from store.models import Store
from rest_framework import viewsets
from store.serializers import StoreSerializer, StorefeesSerializer

class StoreViewSet(viewsets.ModelViewSet):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer

class StorefeesViewSet(viewsets.ModelViewSet):
	queryset = Storefees.objects.all()
	serializer_class = StorefeesSerializer


