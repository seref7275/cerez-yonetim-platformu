from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Giriş başarılıysa ana sayfaya yönlendirin
        else:
            return HttpResponse("Invalid login credentials")  # Hata mesajı döndürün
    return render(request, 'login.html')  # Hazır HTML dosyanızı buraya koyun
