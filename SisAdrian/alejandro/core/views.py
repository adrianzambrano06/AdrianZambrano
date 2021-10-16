from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import *
# Create your views here.



def inicio(request):
    return render(request,'bienvenidos.html')
def registroUsuario(request):
    if request.method == "POST":
        nombreUsuario = request.POST['nombreUsuario']
        Email = request.POST['correo']
        pwd = request.POST['password']
        Edad = request.POST['edad']
        Genero = request.POST['genero']
        Estado = request.POST['estado']
        nuevoUsuario(nombreUsuario=nombreUsuario, Email=Email, pwd=pwd, Edad=Edad, Genero=Genero, Estado=Estado).save()
        messages.success(request, 'El usuario' + request.POST['nombreUsuario'] + 'se registro exitosamente')
        return render(request, 'loguearse/registrarse.html')
    else:
        return render(request, 'loguearse/registrarse.html')


def paginalogin(request):
    if request.method == "POST":
        try:
            detalleUsuario = nuevoUsuario.objects.get(Email=request.POST['correo'], pwd=request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['Email'] = detalleUsuario.Email
            return render(request, 'bienvenidos.html')
        except nuevoUsuario.DoesNotExist as e:
            messages.success(request, 'Correo o Password no es correcto')
    return render(request, 'loguearse/login.html')


