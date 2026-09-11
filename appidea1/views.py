from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import ProductForm
from .models import Product


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            # Not on the add form — start full: current == actual
            product.current_weight_kg = product.actual_weight_KG
            product.save()
            return redirect('levels')
    else:
        form = ProductForm()

    return render(request, 'addnew.html', {'form': form})


def home(request):
    return redirect('add_product')


def levels(request):
    products = Product.objects.all().order_by('product_location', 'product_name')
    return render(request, 'levels.html', {'products': products})


def control_panel(request):
    products = Product.objects.all().order_by('product_location', 'product_name')
    return render(request, 'controlpanel.html', {'products': products})


@require_POST
def clear_database(request):
    """Wipe all products (keeps empty tables / migrations)."""
    Product.objects.all().delete()
    return redirect('control_panel')
