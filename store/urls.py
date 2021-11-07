from django.urls import path
from . import views
# from rest_framework.views import obtain_auth_token

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    # path('login', obtain_auth_token, name="login"),
]
