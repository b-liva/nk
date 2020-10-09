from django import forms
import django_filters
from recipient.models import Recipient


class RecFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(
        lookup_expr='icontains',
        label='مددجو',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Recipient
        fields = ['last_name']
