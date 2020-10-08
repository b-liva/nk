import django_filters
from supporter.models import Supporter


class SupporterFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Supporter
        fields = ['is_active', 'gender', 'caseworker']
