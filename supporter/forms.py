from django import forms
from supporter.models import Supporter, Contact


class SupporterForm(forms.ModelForm):
    class Meta:
        model = Supporter
        fields = ('gender', 'first_name', 'last_name', 'caseworker',)

        labels = {
            'gender': ('0'),
            'first_name': ('نام'),
            'last_name': ('نام خانوادگی'),
            'caseworker': ('مددجو'),
        }

        widgets = {
            'gender': forms.Select(attrs={
                'class': 'form-control',
            }),
            'caseworker': forms.Select(attrs={
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
            'mobile': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره تماس'
            }),
            # '': forms.DateInput(attrs={
            #     'class': 'datetime-input form-control',
            #     'id': 'date_fa'
            # }),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('phone', 'mobile',)

        labels = {
            'phone': ('تلفن',),
            'mobile': ('موبایل',),
        }

        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'تلفن'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موبایل'
            })
        }
