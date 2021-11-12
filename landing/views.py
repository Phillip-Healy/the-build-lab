from django.shortcuts import render
from .models import Customer, Payment, Content


def index(request):
    """ View function for home page """

    return render(request, 'index.html')
