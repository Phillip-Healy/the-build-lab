""" payments/urls.py """

from django.urls import path

from . import views

urlpatterns = [
    path('', views.payments, name='payments'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
]
