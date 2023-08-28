from django.urls import path, include
from rest_framework import routers
from .views import OrderModelViewSet

order_router = routers.SimpleRouter()
order_router.register(r'', OrderModelViewSet)


urlpatterns = [
    path('', include(order_router.urls)),
]