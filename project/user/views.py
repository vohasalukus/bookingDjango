from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect

from user.forms import SignUpForm, SignInForm


def register(request):
    if request.user.is_authenticated:
        return redirect('list_of_rooms')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_of_rooms')
    return render(
        request,
        'user/register.html',
        context={
            'form': SignUpForm()
        }
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect('list_of_rooms')
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_of_rooms')
    return render(
        request,
        'user/login.html',
        context={
            'form': SignInForm()
        }
    )


def logout_view(request):
    logout(request)
    return redirect('login')
