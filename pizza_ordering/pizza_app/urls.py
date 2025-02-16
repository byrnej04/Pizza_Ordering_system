from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_overview, name='order_overview'),
    path('create-pizza/', views.create_pizza, name='create_pizza'),
    path('cart/', views.cart, name='cart'),
    path('order-details/', views.order_details, name='order_details'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('register/', views.register, name='register'),
]
