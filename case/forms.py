from django import forms
from case.models import Illness


class IllnessModelForm(forms.ModelForm):
    class Meta:
        model = Illness
        fields = ('title',)

        labels = {
            'title': ('عنوان بیماری'),
        }