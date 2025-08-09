from django.db import models

# Create your models here.

class ClothingItem(models.Model):
    CATEGORY_CHOICES = [
        ('SUIT', 'Suit'),
        ('ROBE', 'Robe'),
        ('TUX', 'Tuxedo'),
        ('GOWN', 'Gown'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='clothing_images/')
    model_3d = models.FileField(upload_to='models_3d/', blank=True, null=True)

    def __str__(self):
        return self.name