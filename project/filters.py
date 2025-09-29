import django_filters
from home.models import Residential, Locality   # ✅ sahi import

class ResidentialFilter(django_filters.FilterSet):
    locality = django_filters.ModelChoiceFilter(
        queryset=Locality.objects.all(),
        field_name="locality",
        label="Locality"
    )

    class Meta:
        model = Residential
        fields = ['locality']