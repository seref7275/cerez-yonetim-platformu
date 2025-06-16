# api/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    
]

# api/models.py
from django.db import models

class Item(models.Model):
    # Define your model fields here
    pass

# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',  # Use 'api' instead of 'users'
]