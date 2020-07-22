from django import forms
from supporter.models import Supporter


class SupporterForm(forms.ModelForm):
    class Meta:
        model = Supporter
        fields = ('gender', 'first_name', 'last_name', 'mobile',)

        labels = {
            'gender': ('0'),
            'first_name': ('نام'),
            'last_name': ('نام خانوادگی'),
            'mobile': ('شماره تماس'),
        }