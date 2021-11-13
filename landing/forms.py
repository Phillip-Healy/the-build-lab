""" Form control for landing app """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class RegisterForm(UserCreationForm):
    """ Customer user registration form """
    email = forms.EmailField(
        required=True, help_text= 'Enter Email',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )

    username = forms.CharField(
        max_length= 200,
        required = True,
        help_text= 'Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        )

    password1 = forms.CharField(
        help_text='Enter Password',
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        )

    password2 = forms.CharField(
        required = True,
        help_text= 'Enter Password Again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
        )

    check = forms.BooleanField(required = True)

    class Meta:
        model = User
        fields = [
            "username", "email", "password1", "password2", 'check'
            ]
