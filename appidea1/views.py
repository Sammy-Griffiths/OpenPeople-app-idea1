from django.shortcuts import render
from .models import ChemicalLevels

# Create your views here.
def home(request):
    return render(request, 'base.html')

def levels(request):
    items = ChemicalLevels.objects.all().order_by('location', 'number')
    return render(request, 'levels.html', {'levels': items})

