""" Views for landing app """
import stripe

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views import View
from django.contrib.auth import login
from django.conf import settings
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Payment, Content, Price, Product
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


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
        return redirect('payments')


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


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "https://8000-amaranth-chimpanzee-hy17mdxs.ws-eu18.gitpod.io/"  # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "success.html"
    # On a live payment this would then check payment is complete and change user group


class CancelView(TemplateView):
    template_name = "cancel.html"


class ProductLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Premium")
        prices = Price.objects.filter(product=product)
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context
