from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') # Redirige a la página de inicio después del login exitoso
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'usuarios/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Usuario registrado exitosamente')
            return redirect('login')
    return render(request, 'usuarios/register.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, '')
    return redirect('index')

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'usuarios/perfil.html', {'user': user})
