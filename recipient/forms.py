from django import forms
from recipient.models import Recipient


class RecipientModelForm(forms.ModelForm):

    class Meta:
        model = Recipient
        fields = ('gender', 'first_name', 'last_name')

        labels = {
            'gender': (''),
            'first_name': ('نام'),
            'last_name': ('نام خانوادگی'),
        }

        widgets = {
            'gender': forms.Select(attrs={
                'class': 'form-control',

            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام',

            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانودادگی',
            }),
        }

