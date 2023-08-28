from rest_framework import viewsets
from ...shared.pagination import PageLimitPagination
from ..models import Order
from ..serializers import OrderModelSerializer
# from ...shared.util import get_exclude_query
# from django_filters.rest_framework import DjangoFilterBackend
# from ..filters import ProductFilter



class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    pagination_class = PageLimitPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter
    # filterset_fields  = '__all__'

    # def get_queryset(self):
    #     ordering = self.request.GET.get('_sort', "id")
    #     queryset_order = self.queryset.order_by(ordering)
    #     queryset_exclude = Product.objects.exclude(
    #         **get_exclude_query(self.request.GET))
    #     return queryset_order & queryset_exclude