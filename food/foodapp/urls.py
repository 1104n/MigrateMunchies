from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
1
urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path("foodapp/", include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),


]
