from django import forms
import django_filters
from caseworker.models import CaseWorker


class CwFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(
        lookup_expr='icontains',
        label='مددکار',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'مددکار'
        })
    )

    class Meta:
        model = CaseWorker
        fields = ['last_name']
