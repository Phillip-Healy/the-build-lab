from django.urls import path
from . import views
from .views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    ProductLandingPageView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('games/', views.games, name='games'),
    path('premium/', views.premium, name='premium'),
    path('register/', views.register, name='register'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('payments', ProductLandingPageView.as_view(), name='payments'),
]
