"""
URL configuration for LibraryManagement project.

The `urlpatterns` list routes URLs to views. For more information, see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Importing HttpResponse for a simple view

# A simple home view for the root URL
def home_view(request):
    return HttpResponse("Welcome to the Library Management System API!")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin dashboard route
    path('api/', include('library.urls')),  # Including routes from the 'library' app
    path('', home_view, name='home'),  # Route for the homepage view
]
