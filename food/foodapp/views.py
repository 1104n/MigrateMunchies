from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def login_auth(request):
    print("in")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'store/store.html')
        # Redirect to a success page.
        else:
            print("okay")
            return HttpResponseRedirect(reverse('login'))
    print("ok")
    return render(request, 'registration/login.html')

def home(request):
    print("in")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'store/home.html')
        # Redirect to a success page.
        else:
            print("okay")
            return HttpResponseRedirect(reverse('login'))
    print("ok")
    return render(request, 'registration/login.html')
