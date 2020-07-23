from django import forms
from caseworker.models import CaseWorker


class CaseWorkerModelForm(forms.ModelForm):

    class Meta:
        model = CaseWorker
        fields = ('gender', 'first_name', 'last_name', 'is_active',)

        labels = {
            'gender': 'عنوان',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'is_active': 'فعال',
        }