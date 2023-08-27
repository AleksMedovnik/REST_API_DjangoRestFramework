from rest_framework import viewsets
from ..models import Product
from ...shared.pagination import PageLimitPagination
from ...shared.util import get_exclude_query
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import ProductFilter
from ..serializers import ProductModelSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = PageLimitPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    # filterset_fields  = '__all__'

    def get_queryset(self):
        ordering = self.request.GET.get('_sort', "id")
        queryset_order = self.queryset.order_by(ordering)
        queryset_exclude = Product.objects.exclude(
            **get_exclude_query(self.request.GET))
        return queryset_order & queryset_exclude


# class CustomerAPIView(APIView, PageOffsetLimitPagination):

#     def get(self, request, **kwargs):
#         pk = kwargs.get('pk', None)
#         if pk:
#             try:
#                 instance = Customer.objects.get(pk=pk)
#             except:
#                 return Response({'Error': 'The object does not exist'})
#             serializer = CustomerSerializer(instance)
#         else:
#             ordering = request.GET.get('_sort', 'pk')
#             queryset = self.paginate_queryset(
#                 Customer.objects.filter(
#                     **get_filter_query(request.GET)
#                 ).order_by(ordering) 
#                 &
#                 Customer.objects.exclude(**get_exclude_query(request.GET)),
#                 request,
#                 view=self
#             )
#             serializer = CustomerSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         # serializer = CustomerSerializer(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data)
#         return Response({**request.data, 'id': len(Customer.objects.all())+1})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'Error': 'Method "PUT" not allowed.'})
#         # try:
#         #     instance = customer_models.Customer.objects.get(pk=pk)
#         # except:
#         #     return Response({'Error': 'The object does not exist'})
#         # serializer = CustomerSerializer(data=request.data, instance=instance)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data)
#         return Response(request.data)

#     def patch(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'Error': 'Method "PATCH" not allowed.'})
#         # try:
#         #     instance = customer_models.Customer.objects.get(pk=pk)
#         # except:
#         #     return Response({'Error': 'The object does not exist'})
#         # serializer = CustomerSerializer(data=request.data, instance=instance, partial=True)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data)
#         return Response(request.data)

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'Error': 'Method "DELETE" not allowed.'})
#         try:
#             instance = Customer.objects.get(pk=pk)
#         except:
#             return Response({'Error': 'The object does not exist'})
#         # instance.delete()
#         return Response({'response': f'Client "{instance.nick}" deleted'})