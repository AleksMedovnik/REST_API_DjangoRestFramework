from django.urls import path, include
from rest_framework import routers
from .views import ProductModelViewSet

product_router = routers.SimpleRouter()
product_router.register(r'', ProductModelViewSet)


urlpatterns = [
    path('', include(product_router.urls)),
]