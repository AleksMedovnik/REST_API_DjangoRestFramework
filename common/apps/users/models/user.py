from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    date_birth = models.DateField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)

    REQUIRED_FIELDS = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'date_birth',
        'country',
        'city',
        'district',
    )