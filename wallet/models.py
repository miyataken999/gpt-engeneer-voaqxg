from django.db import models

class Wallet(models.Model):
    brand_name = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_place = models.CharField(max_length=255)
    accessory = models.CharField(max_length=255)
    precious_metal_purity = models.CharField(max_length=255)
    precious_metal_weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.brand_name