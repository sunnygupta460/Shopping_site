from django.db import models
from django.contrib.auth.models import User
#from order.models import Marketplace


class Store(models.Model):
    # marketplace = models.ForeignKey(Marketplace, related_name='marketplace_store')
    # user = models.ForeignKey(User, related_name='user_store')
    # user = models.OneToOneField(User, primary_key=True, default='SOME STRING')
    name = models.CharField(max_length=250)
    api_key = models.CharField(max_length=250, default='SOME STRING')
    user_key = models.CharField(max_length=500, default='SOME STRING')
    store_key = models.CharField(max_length=500, default='SOME STRING')

    def __str__(self):
        return self.name


class Storefees(models.Model):
    store_id = models.ForeignKey(Store, related_name='storefees_store', on_delete=models.CASCADE)
    store_type = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.store_type
