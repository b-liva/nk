from django import forms
from recipient.models import Recipient


class RecipientModelForm(forms.ModelForm):

    class Meta:
        model = Recipient
        fields = ('first_name', 'last_name')

        labels = {
            'first_name': ('نام'),
            'last_name': ('نام خانوادگی'),
        }
