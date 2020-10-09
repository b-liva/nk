from django import forms
import django_filters
from case.models import Illness, Case
from recipient.models import Recipient


class IllnessFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='بیماری',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'بیماری'
        })
    )

    class Meta:
        model = Illness
        fields = ['title']


class CaseFilter(django_filters.FilterSet):
    recipient = django_filters.ModelChoiceFilter(
        queryset=Recipient.objects.all(),
        label='مددجو',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'مددجو'
        }),
        empty_label='انتخاب مددجو'
    )
    illness = django_filters.ModelMultipleChoiceFilter(
        queryset=Illness.objects.all().order_by('title'),
        label='بیماری',
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-inline px-3',
            'placeholder': 'بیماری'
        })
    )

    class Meta:
        model = Case
        fields = ['recipient', 'illness']
