from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
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
        fields = ('recipient', 'illness', 'date',  'description',)

        labels = {
            'recipient': 'بیمار',
            'illness': 'بیماری',
            'date': 'تاریخ',
            'description': 'توضیحات',
        }

    def __init__(self, *args, **kwargs):
        super(CaseModelForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(
            label= ('تاریخ'),
            widget=AdminJalaliDateWidget
        )
