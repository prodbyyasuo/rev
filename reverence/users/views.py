from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import (
    UserRegistrationForm,
    UserAuthenticationForm,
    UserProfileForm
    )
from django.contrib.auth.decorators import login_required
# from orders.models import Order


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:catalog')
    else:
        form = UserAuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


@login_required(login_url='/users/login')
def user_logout(request):
    login(request)
    return redirect('users:login')
