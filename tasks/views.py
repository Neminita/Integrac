from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
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
