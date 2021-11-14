""" Models to generate the database """
import datetime

from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing
from django.conf import settings
from django.contrib.auth.models import User

class Payment(models.Model):
    """ Model for tracking and storing payments """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=19.99)
    complete = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this Payment."""
        return reverse('Payment-detail', args=[str(self.id)])


class Content(models.Model):
    """ Model for storing content for distribution accross site"""
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
