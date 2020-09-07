from django.http import HttpResponse
from django.shortcuts import render
import os

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request, os.getcwd())
    return render(request, "index.html", {})
