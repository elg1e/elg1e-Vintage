from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    GENDER_CHOICES = [
        ('mens','mens'),
        ('womens','womens')
    ]
    gender = models.CharField(choices=GENDER_CHOICES, default='mens')
    CLOTHING_TYPE = [
        ('tops','tops'),
        ('shirts','shirts'),
        ('jumpers','jumpers'),
        ('jeans','jeans'),
        ('accessories','accessories'),
    ]
    clothingType = models.CharField(choices='CLOTHING_TYPE', default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name