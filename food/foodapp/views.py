from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import login


# Create your views here.
def store(request) :
    context = {}
    return render(request, 'home.html', context)


def cart(request) :
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request) :
    context = {}
    return render(request, 'store/checkout.html', context)


def home(request) :
    return render(request, 'home.html', {})


def register(request) :
    if request.method == 'POST' :
        a = request.POST.get('username')
        b = request.POST.get('password1')
        print(a)
        print(b)
        form = UserCreationForm(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "account created successfully")
            return redirect('home')
        else :
            form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    form = UserCreationForm()
    return render(request, 'registration/register.html', context={"form": form})
