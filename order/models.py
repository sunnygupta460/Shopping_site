from django.db import models
from product.models import Product

class Order(models.Model):
    pro_id = models.ForeignKey(Product, related_name='order')
    orderdate = models.DateTimeField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    orderstatus = models.BooleanField(default=True)

    def __str__(self):
        return self.quantity
