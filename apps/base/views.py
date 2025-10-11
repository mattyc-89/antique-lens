from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import MyUserCreationForm, UserLoginForm

# Create your views here.

def loginUser(request):
    form = UserLoginForm()

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            
            identifier = request.POST.get("email").lower()
            password = request.POST.get("password")
            
            user = authenticate(request, username=identifier, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                messages.error(request, "Account is inactive.")
            else:
                messages.error(request, "Invalid credentials.")
    
    return render(request, "auth-login.html", {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')


def register(request):
    form = MyUserCreationForm()


    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Call the save method of the form
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration.")

    return render (request, "auth-signup.html", {'form': form})


def home(request):
   return render(request, 'index.html')

