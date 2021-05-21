from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext as _

from commitment.models import Commitment
from supporter.models import Supporter


class CommitmentModelForm(forms.ModelForm):

    class Meta:
        model = Commitment
        fields = ('amount', 'date',)

        labels = {
            'date': 'تاریخ',
            'amount': 'مبلغ',
        }

        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(CommitmentModelForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(
            label=_('تاریخ'),  # date format is  "yyyy-mm-dd",
            widget=AdminJalaliDateWidget,  # optional, to use default datepicker
        )
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] += ' form-control'
