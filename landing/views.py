from django.shortcuts import render
from .models import Customer, Payment, Content


def index(request):
    """ View function for home page """

    return render(request, 'index.html')


def news(request):
    """ View function for news page """

    return render(request, 'news.html')


def games(request):
    """ View function for games page """

    return render(request, 'games.html')


def premium(request):
    """ View function for premium page """

    # Generate data from DB
    contents = Content.objects.all()
    context = {'contents': contents}
    return render(request, 'premium.html', context)
