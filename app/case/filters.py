import django_filters
from case.models import Illness, Case


class IllnessFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Illness
        fields = ['title']


class CaseFilter(django_filters.FilterSet):

    class Meta:
        model = Case
        fields = ['recipient', 'illness']
