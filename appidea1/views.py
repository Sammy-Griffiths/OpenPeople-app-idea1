from django.shortcuts import render, redirect
from .forms import AddProductForm
from .models import ChemicalLevels

# Create your views here.

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_chemical")
    else:
        form = AddProductForm()

    return render(request, 'addnew.html', {'form': form})

def home(request):
    return render(request, 'base.html')

def levels(request):
    items = ChemicalLevels.objects.all().order_by('location', 'number')
    return render(request, 'levels.html', {'levels': items})

