from django.db import models
from decimal import Decimal

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
    (2, 'Milliliters'),
]

PRODUCT_COLORS = [
    (0, 'Blue'),
    (1, 'Orange'),
    (2, 'Green'),
    (3, 'Gray'),
    (4, 'Yellow'),
    (5, 'Purple'),
    (6, 'Brown'),
    (7, 'Pink'),
    (8, 'Cyan'),
    (9, 'White'),
    (10, 'Red'),
]

# Empty container weight in kg, keyed by jug size in liters.
container_weight = {
    20: 2.5,
    4: 0.8,
}

# How many liters are in one unit of each volume_unit choice.
LITERS_PER_UNIT = {
    0: Decimal('1'),          # Liters
    1: Decimal('3.78541'),    # Gallons (US) to liters
    2: Decimal('0.001'),      # Milliliters to liters
}


class Product(models.Model):
    """One row per product shown on Product Levels / control panel."""

    product_name = models.CharField(max_length=200)
    product_location = models.IntegerField(choices=RESTAURANT_LOCATIONS, default=0)
    volume_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    volume_unit = models.IntegerField(choices=UNIT_OF_PRODUCT, default=0)
    density = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    color = models.IntegerField(choices=PRODUCT_COLORS, default=0)
    # Live scale weight; not on add form. Starts as actual_weight_kg; control panel later.
    current_weight_kg = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        ordering = ['product_location', 'product_name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name

    @property
    def color_css(self):
        """CSS class suffix from the color choice label, e.g. 'red'."""
        return self.get_color_display().lower()

    @property
    def volume_amount_l(self):
        """Convert stored volume_amount into liters."""
        factor = LITERS_PER_UNIT.get(self.volume_unit, Decimal('1'))
        return Decimal(self.volume_amount) * factor

    @property
    def actual_weight_kg(self):
        """
        actual_weight_kg = (volume_amount_l * density) + container_weight[volume_amount_l]
        """
        liters = self.volume_amount_l
        key = int(liters) if liters == int(liters) else float(liters)
        empty_kg = Decimal(str(container_weight.get(key, container_weight.get(int(liters), 0))))
        return (liters * Decimal(self.density)) + empty_kg