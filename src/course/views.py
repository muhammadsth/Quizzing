from django.http import HttpResponse
from django.shortcuts import render
import os
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CourseForm
from django.contrib.auth.forms import AuthenticationForm

def add_course_view(request):
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
    return render(request, "add-course.html", {"course_form": CourseForm})
