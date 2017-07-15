from django import forms
from .models import Twitt

class TwittForm(forms.ModelForm):

    class Meta:
        model = Twitt
        fields = [
            'text',
        ]

        labels = {
            'text':'¿ Que estas pensando ?',
        }

        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control'}),
        }