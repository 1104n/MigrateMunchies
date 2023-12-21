from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout


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


def login_auth(request) :
    if request.method == 'POST' :
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid() :
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request, user)
                return redirect('home')
    form = AuthenticationForm()
    return render(request, "registration/login.html", context={"form" : form})


def register(request) :
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('password1')
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            messages.success(request, "account created successfully")
            return redirect('home')
        else:
            form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    form = UserCreationForm()
    return render(request, 'registration/register.html', context={"form": form})
