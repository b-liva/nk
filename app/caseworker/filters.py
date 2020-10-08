import django_filters
from caseworker.models import CaseWorker


class CwFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CaseWorker
        fields = ['is_active', 'gender']
