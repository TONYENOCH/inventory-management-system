from django.db import models
from django.conf import settings

# Create your models here.
class Items(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, default="")
    price = models.DecimalField(null=False, blank=False, max_digits=15, default=0, decimal_places=2)
    
class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_id = models.UUIDField()