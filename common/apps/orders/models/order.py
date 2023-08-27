from django.db import models
from .models import DeliveryMethod, PaymentMethod


class Order(models.Model):
    title = models.CharField(max_length=255)
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
    customer = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        related_name='orders'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.PROTECT,
        related_name='orders'
    )

    def __str__(self) -> str:
        return self.title