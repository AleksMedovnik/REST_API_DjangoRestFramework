from django.contrib import admin
from .models import Color, Maker, OS, RAM


admin.site.register((Color, Maker, OS, RAM))