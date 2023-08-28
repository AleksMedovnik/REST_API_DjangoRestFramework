from django.contrib import admin
from .models import DeliveryMethod, PaymentMethod


admin.site.register((DeliveryMethod, PaymentMethod))