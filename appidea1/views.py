from django.shortcuts import render, redirect
from .forms import AddChemicalForm
from .models import ChemicalLevels

# Create your views here.

def add_chemical(request):
    if request.method == 'POST':
        form = AddChemicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_chemical")
    else:
        form = AddChemicalForm()

    return render(request, 'addnew.html', {'form': form})

def home(request):
    return render(request, 'base.html')

def levels(request):
    items = ChemicalLevels.objects.all().order_by('location', 'number')
    return render(request, 'levels.html', {'levels': items})

