from django.db import models
from product.models import Product


class Order(models.Model):
    pro_id = models.ForeignKey(Product, related_name='order', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    order_status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.quantity)


class Marketplace(models.Model):
    name = models.CharField(max_length=100)
    conn_method = models.CharField(max_length=45)

    def __str__(self):
        return self.name
