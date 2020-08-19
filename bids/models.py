from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class bidding(models.Model):
    product = models.ForeignKey(Product, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bids = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)])
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(default=datetime.datetime.now, auto_now=False, auto_now_add=False)