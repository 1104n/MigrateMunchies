from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.store, name='store'),
    path('login', views.login_auth, name='login'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),


]
