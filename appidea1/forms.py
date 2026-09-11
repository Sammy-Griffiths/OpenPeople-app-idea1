from django import forms
from .models import AddProduct

class AddProductForm(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = ['product_name','product_location', 'volume_amount', 'volume_unit', 'density']