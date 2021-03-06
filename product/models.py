from django.db import models
from store.models import Store

class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, related_name='store_product')
    stock = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    pro_id = models.ForeignKey(Store, related_name='purchase_product')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    orderdate = models.DateTimeField(auto_now_add=True)
    amountpaid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.quantity
