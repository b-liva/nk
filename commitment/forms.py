from django import forms
from commitment.models import Commitment


class CommitmentModelForm(forms.ModelForm):
    class Meta:
        model = Commitment
        fields = ('case', 'supporter', 'amount',)

        labels = {
            'case': '',
            'supporter': '',
            'amount': '',
        }