from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing


class Customer(models.Model):
    """ Model representing users on the system """
    name = models.CharField(max_length=40, help_text='Please Enter Your Name:')
    email = models.EmailField(max_length=100)
    premium = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this User."""
        return reverse('User-detail', args=[str(self.id)])


class Payment(models.Model):
    """ Model for tracking and storing payments """
    user = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=19.99)
    complete = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Payment."""
        return reverse('Payment-detail', args=[str(self.id)])


class Content(models.Model):
    """ Model for storing content for distribution accross site"""
    name = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
