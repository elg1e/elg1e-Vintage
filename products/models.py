from django.db import models

# Create your models here.

class Product(models.Model):
    GENDER_CHOICES = [
        ('mens','mens'),
        ('womens','womens')
    ]
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='mens')
    CLOTHING_TYPE = [
        ('tops','tops'),
        ('shirts','shirts'),
        ('jumpers','jumpers'),
        ('jeans','jeans'),
        ('accessories','accessories')
    ]
    clothingType = models.CharField(max_length=50, choices=CLOTHING_TYPE, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    buyout = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name