from django.db import models
from django import forms
import django_filters
from django.forms import SelectMultiple

from caseworker.models import CaseWorker
from supporter.models import Supporter


class SupporterFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['caseworker'].widget.attrs = {
            'class': 'form-control'
        }

    last_name = django_filters.CharFilter(
            lookup_expr='icontains',
            label='حامی',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    caseworker = django_filters.ModelChoiceFilter(
        queryset=CaseWorker.objects.all().order_by('last_name'),
        empty_label='انتخاب مددکار'
    )

    class Meta:
        model = Supporter
        fields = ['caseworker', 'last_name']

