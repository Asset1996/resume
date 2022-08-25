"""
Views for user app.
"""
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def Register(request):
    """Registering view for registering the new user."""
    form = RegisterForm()
    template_name = 'register.html'

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_email = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + user_email)
            return redirect('main:home')
    
    context = {'form': form}

    return render(request, template_name, context)

def Login(request):
    """Login view for authenticating the user."""
    form = LoginForm()
    template_name = 'login.html'

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in as ' + email)
                return redirect('main:home')
            else:
                messages.error(request, 'Incorrect password or email')
    
    context = {'form': form}

    return render(request, template_name, context)

@login_required
def Logout(request):
    """Logging out the authenticated user."""
    logout(request)
    return redirect('user:login')
