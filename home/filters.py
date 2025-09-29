# project/filters.py
import django_filters
from project.models import Residential   # 👈 yahan se import karo
from utility.models import Locality   # 👈 yahan se import karo

class ResidentialFilter(django_filters.FilterSet):
    locality = django_filters.ModelChoiceFilter(
        queryset=Locality.objects.all(),
        field_name="locality",
        label="Locality"
    )

    class Meta:
        model = Residential
        fields = ['locality']
