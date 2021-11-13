""" Form control for landing app """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class NewCustomerForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Customer
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        customer = super(NewCustomerForm).save(commit=False)
        customer.email = self.cleaned_data['email']
        if commit:
            customer.save()
        return customer
