from django.db import models


class DeliveryMethod(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'delivery_method'


class PaymentMethod(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'payment_method'