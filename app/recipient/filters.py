import django_filters
from recipient.models import Recipient


class RecFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Recipient
        fields = ['is_active', 'gender']
