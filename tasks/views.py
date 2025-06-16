from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView

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
    context = {
        'products' : Product.objects.all()
    }
    return render(request, 'home.html', context)

def base(request):
    return render(request, 'base.html',)

def tasks(request):
    return render(request, 'tasks.html',)

def create_task(request):

    if request.method == 'GET':
        return render(request, 'create_task.html',{
            'form' : TaskForm
        }) 
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html',{
                'form' : TaskForm,
                'error' : 'Datos inválidos'
            }) 




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


def product_list(request):
    context = {
        'products' : Product.objects.all()
    }
    return render(request, 'product_list.html', context)

def products(request):
    return render(request, 'products.html',)

def carrito(request):
    return render(request, 'carrito.html',)