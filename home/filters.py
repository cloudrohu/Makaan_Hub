import django_filters
from project.models import Residential

class ResidentialFilter(django_filters.FilterSet):
    locality = django_filters.CharFilter(field_name='locality__name', lookup_expr='icontains')

    class Meta:
        model = Residential
        fields = ['locality']
