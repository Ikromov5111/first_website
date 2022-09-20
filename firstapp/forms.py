from django import forms
from .models import Check


class CreateCheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields='__all__'