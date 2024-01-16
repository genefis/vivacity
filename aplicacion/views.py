from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from.models import eventos
from.models import canton


def index(request):
    return render(request,'index.html')


def registro(request):
    return render(request,'registro.html')


#Registro
def signup(request):
    print('Estoy en el registro')
    if request.method == 'GET':
        return render(request, 'registro.html', {
            # Quiero que sea un formulario de registro de usuario con los campos de usuario, contraseña y correo electrónico
            "form": UserCreationForm
            
            })
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                print(request.POST["username"])
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"], email=request.POST["email"])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'registro.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'registro.html', {"form": UserCreationForm, "error": "Passwords did not match."})
    

# Iniciar sesion
def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('eventos')
    
def eventos(request):
    return render(request,'eventos.html')


def tour(request):
    return render(request,'tour.html')



def hospedaje(request):
    return render(request,'hospedaje.html')

def lugares(request):
    return render(request,'lugares.html')

def salir(request):
    return render(request,'salir.html')


def listarCanton(request):
    busqueda = request.GET.get("buscar")
    cantones = canton.objects.all()

    if busqueda:
        cantones = canton.objects.filter(
            Q(nombre_canton__icontains = busqueda) 
        ).distinct()
    return render(request,"eventos.html",{"cantones":cantones})
