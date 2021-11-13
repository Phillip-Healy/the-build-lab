from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Payment, Content


def index(request):
    """ View function for home page """

    if request.user.is_authenticated:
        user = request.user.get_username
        context = {'user': user}
    else:
        context = {}

    return render(request, 'index.html', context)


def news(request):
    """ View function for news page """

    return render(request, 'news.html')


@login_required
def games(request):
    """ View function for games page """

    return render(request, 'games.html')


@login_required
def premium(request):
    """ View function for premium page """

    # Generate data from DB
    contents = Content.objects.all()
    context = {'contents': contents}

    if request.user.groups.filter(name__in=['premium']).exists():
        return render(request, 'premium.html', context)
    else:
        return redirect('index')


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('index')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})
