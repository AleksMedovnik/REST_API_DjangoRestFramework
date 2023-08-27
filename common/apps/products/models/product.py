from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Color, Maker, OS, RAM


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    info = models.TextField(blank=True) 
    price = models.FloatField(
        default=0,
        validators=[
            MaxValueValidator(1000000000.00),
            MinValueValidator(0)
        ]
    )
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    screen_diagonal = models.FloatField()
    battery_capacity = models.IntegerField()
    resolution_main_camera = models.FloatField()
    maker = models.ForeignKey(Maker, on_delete=models.PROTECT, related_name='products')
    os = models.ForeignKey(OS, on_delete=models.PROTECT, related_name='products')
    ram = models.ForeignKey(RAM, on_delete=models.PROTECT, related_name='products')

    class Meta:
        db_table = 'Product'