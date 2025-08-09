from django.db import models

# Create your models here.

class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField() # cm
    chest = models.FloatField()
    waist = models.FloatField()
    hips = models.FloatField()
    arm_length = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class ClothingItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # e.g., suit, dress
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    chest = models.FloatField() # cm
    waist = models.FloatField()
    length = models.FloatField()
    sleeve_length = models.FloatField(null=True, blank=True)
    stock = models.PositiveIntegerField()