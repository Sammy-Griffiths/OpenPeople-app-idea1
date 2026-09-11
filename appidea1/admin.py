from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'product_location',
        'volume_amount',
        'volume_unit',
        'density',
        'color',
        'current_weight_kg',
    )
