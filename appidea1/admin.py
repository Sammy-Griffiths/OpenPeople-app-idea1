from django.contrib import admin
from .models import ChemicalLevels

# Register your models here.

@admin.register(ChemicalLevels)
class ChemicalLevelsAdmin(admin.ModelAdmin):
    list_display = ('location', 'label', 'number', 'weight')

# next things to add would be inputting data and css