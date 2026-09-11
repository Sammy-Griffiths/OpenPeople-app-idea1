from django.db import models

# Create your models here.

RESTAURANT_LOCATIONS = [
        (0, 'Kitchen'),
        (1, 'Bar'),
        (2, 'Dish Pit'),
        (3, 'Basement'),
        (4, 'Upstairs'),
    ]

UNIT_OF_PRODUCT = [
    (0, 'Liters'),
    (1, 'Gallons'),
    (2, 'Milliliters')
    ]

class AddProduct(models.Model):
    product_name = models.CharField(max_length=30)
    product_location = models.IntegerField(choices=RESTAURANT_LOCATIONS, default=0)
    volume_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    volume_unit = models.IntegerField(choices=UNIT_OF_PRODUCT, default=0)
    density = models.DecimalField(max_digits=3, decimal_places=2, default=1)

class ChemicalLevels(models.Model):

    location = models.IntegerField(choices=RESTAURANT_LOCATIONS, default=0)
    label = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ['location', 'number']

