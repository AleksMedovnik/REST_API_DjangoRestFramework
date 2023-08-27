import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    pk = django_filters.BaseInFilter(field_name='id')
    title_like = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains'
    )
    info = django_filters.CharFilter(
        field_name='info',
        lookup_expr='icontains'
    )
    price = django_filters.RangeFilter()
    screen_diagonal = django_filters.RangeFilter()
    battery_capacity = django_filters.RangeFilter()
    resolution_main_camera = django_filters.RangeFilter()

    class Meta:
        model = Product
        fields = (
            'pk',
            'id',
            'title',
            'maker',
            'os',
            'color',
            'ram',
        )