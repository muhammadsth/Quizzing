from django.http import HttpResponse
from django.shortcuts import render
import os
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request, os.getcwd())
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect("homepage")
    else:
        return render(request, "index.html", {"signup_form": SignUpForm, "login_form": AuthenticationForm, "messages" : ""})

def homepage_view(request):
    print("redirects to homepage")
    if request.user.is_authenticated:
        return render(request, "index-student.html", {})


def signup_view(request):
    print("does it get posted????")
    if request.method == 'POST':
        print("is it post?")
        # print(request.POST)
        # print(request.body)
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("is it valid?")
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, "index.html", {"signup_form": SignUpForm, "login_form": AuthenticationForm, "messages" : form.errors})
    else:
        form = SignUpForm()
    return redirect('/')


def login_handler(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        print("is it post?")
        # print(request.POST)
        # print(request.body)
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, "index.html", {"signup_form": SignUpForm, "login_form": AuthenticationForm, "messages" : "wrong username or password"})
    else:
        return redirect('/')

def logout_request(request):
    logout(request)
    return redirect("/")
