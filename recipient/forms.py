from django import forms
from recipient.models import Illness, Recipient


class IllnessModelForm(forms.ModelForm):
    class Meta:
        model = Illness
        fields = ('title',)

        labels = {
            'title': ('عنوان بیماری'),
        }


class RecipientModelForm(forms.ModelForm):

    class Meta:
        model = Recipient
        fields = ('first_name', 'last_name', 'illness')

        labels = {
            'first_name': ('نام'),
            'last_name': ('نام خانوادگی'),
            'illness': ('بیماری'),
        }
