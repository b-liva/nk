from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from django.utils.translation import gettext as _
from supporter.models import Supporter, Contact, SupporterCwChange, FollowUp


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


class SupportCwChangeForm(forms.ModelForm):
    class Meta:
        model = SupporterCwChange
        fields = ('new_cw', 'date',)
        labels = {
            'new_cw': ('مدد کار جدید',),
        }

        widgets = {
            'new_cw': forms.Select(attrs={
                'class': ('form-control',)
            }),
        }

    def __init__(self, *args, **kwargs):
        super(SupportCwChangeForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(
            label=_('تاریخ'),  # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget  # optional, to use default datepicker
        )


class FollowUpModelForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = ('date', 'description', 'case')

        labels = {
            'description': ('شرح پیگیری',),
            'case': ('پرونده',)
        }

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(FollowUpModelForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(
            label=_('تاریخ'),  # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget  # optional, to use default datepicker
        )
