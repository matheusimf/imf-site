from django import forms

from .models import SeminarInscription


class SeminarInscriptionForm(forms.ModelForm):
    class Meta:
        model = SeminarInscription
        fields = ['name', 'phone', 'email']
