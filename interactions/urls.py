""" URLs for interactions app """
from django.urls import path
from . import views

urlpatterns = [
    path('future/', views.future, name='future'),
]
