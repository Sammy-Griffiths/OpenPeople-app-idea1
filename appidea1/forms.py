from django import forms
from .models import AddChemical

class AddChemicalForm(forms.ModelForm):
    class Meta:
        model = AddChemical
        fields = ['name']