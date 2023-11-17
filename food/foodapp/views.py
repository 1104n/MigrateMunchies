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
    pass
    # print("in")
    # if request.method == 'POST':
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     print(password)
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('store/store')
    #     # Redirect to a success page.
    #     else:
    #         print("okay")
    #         messages.success(request, 'There was an error')
    #         return redirect('registration/login')
    # print("ok")
    #return render(request, 'registration/login.html')
