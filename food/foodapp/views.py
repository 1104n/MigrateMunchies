from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages


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


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        # Redirect to a success page.
        else:
            messages.success(request, ('There was an error'))
            return redirect('registration/login')
    else:
        context = {}
        return render(request, 'registration/login.html', context)
