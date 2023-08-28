from django.db import models
from .models import DeliveryMethod, PaymentMethod


class Order(models.Model):
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.PROTECT,
        related_name='orders'
    )
    customer = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        related_name='orders'
    )
    delivery_method = models.ForeignKey(
        DeliveryMethod,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.PROTECT,
        related_name='orders'
    )
