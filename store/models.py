
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    address = models.CharField(max_length=500)
    mobile = models.DecimalField(max_digits=13, decimal_places=0)

    def __str__(self):
        return self.name
