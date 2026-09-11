from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_location',
            'volume_amount',
            'volume_unit',
            'density',
            'color',
        ]
        widgets = {
            'product_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'maxlength': '30',
                    'placeholder': 'Product name',
                }
            ),
            'product_location': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'volume_amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01',
                    'min': '0',
                    'placeholder': '1280.00',
                }
            ),
            'volume_unit': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'density': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01',
                    'min': '0',
                    'placeholder': '1.25',
                }
            ),
            'color': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }
