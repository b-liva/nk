from django import forms
from case.models import Illness, Case


class IllnessModelForm(forms.ModelForm):
    class Meta:
        model = Illness
        fields = ('title',)

        labels = {
            'title': ('عنوان بیماری'),
        }


class CaseModelForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('recipient', 'illness', 'description',)

        labels = {
            'recipient': 'بیمار',
            'illness': 'بیماری',
            'description': 'توضیحات',
        }