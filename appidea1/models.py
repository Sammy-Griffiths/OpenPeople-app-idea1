from django.db import models

# Create your models here.

class ChemicalLevels(models.Model):

    RESTAURANT_LOCATIONS = [
        (0, 'Kitchen'),
        (1, 'Bar'),
        (2, 'Dish Pit'),
        (3, 'Basement'),
        (4, 'Upstairs'),
    ]

    location = models.IntegerField(choices=RESTAURANT_LOCATIONS, default=0)
    label = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ['location', 'number']
