from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def signup(request): #FORMULARIO CREACIÓN DE CUENTA

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form' :UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form' :UserCreationForm,
                    'error':'Usuario ya existe'
                })
            
        return render(request, 'signup.html', {
                    'form' :UserCreationForm,
                    'error':'Contraseñas no coinciden'
                })


def home(request):
    return render(request, 'home.html',)

def base(request):
    return render(request, 'base.html',)

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña erróneos'
            })
        else:
            login(request, user)
            return redirect('home')

