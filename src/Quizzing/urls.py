"""Quizzing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from pages.views import homepage_view
from pages.views import signup_view
from pages.views import login_handler
from pages.views import logout_request
from course.views import add_course_view

urlpatterns = [
    path('', home_view, name='home'),
    path('homepage/', homepage_view, name='homepage'),
    path('signup', signup_view, name='signup'),
    path('login', login_handler, name='login'),
    path('logout', logout_request, name='logout'),
    path('addcourse', add_course_view, name='addcourse'),
    path('admin/', admin.site.urls),
]
