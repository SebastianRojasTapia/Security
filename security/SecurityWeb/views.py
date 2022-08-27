# Create your views here.
from re import template
from django.shortcuts import render
from django.contrib.auth.models import User
# adjuntamos la libreria de autenticar 
from django.contrib.auth import authenticate,logout,login as login_autent
#agregar decorador para impedir el ingreso a las paginas sin estar registrado
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
import cx_Oracle #para ocupar varibles de oracle

from datetime import datetime # libreria para saber la fecha actual

# Create your views here.

def logout_vista(request):
    logout(request)
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def login(request):
    data = {
        'rubro':listar_rubro()
    }
    if 'registro' in request.POST:
        rutCliente = request.POST.get('rut')
        razonSocial = request.POST.get('razonSocial')
        numeroContacto = request.POST.get('numeroContacto')
        rubro = request.POST.get('rubro')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('pass')
        try:
            u = User.objects.get(username=razonSocial)
            data['mensaje'] = 'Usuario ya ingresado'
            u = User.objects.get(email=correo)
            data['mensaje'] = 'Correo ya ingresado'
            return render(request,'login.html',data)
        except:
            u = User()
            u.username = razonSocial
            u.email = correo
            u.set_password(contrasena)
            salida = agregar_usuario(rutCliente, razonSocial, numeroContacto, rubro,  correo, u.password)
            u.save()
        if salida == 1:
            data['mensaje'] = 'Se registro correctamente.'
        else:
            data['mensaje'] = 'Error en el registro vuelva intentar.'
        return render(request,'login.html',data)

    elif 'login' in request.POST:
        user = request.POST.get("user")
        password = request.POST.get("pass")
        us = authenticate(request,username=user,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            return render(request,'index.html',{'user':us})
        else:
            return render(request,'login.html',{'msg':'Usuario o contraseña incorrecta'})

    return render(request,'login.html',data)
  
def contacto(request):
    return render(request,'contacto.html')
    
def plan(request):
    return render(request,'plan.html')

def visionMision(request):
    return render(request,'vision-mision.html')

def asesoria(request):
    return render(request,'asesoria.html')


#----------------- Listado -----------------

def agregar_usuario(rutCliente, razonSocial, numeroContacto,rubro,correo,contrasena):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_USUARIO_CLIENTE",[rutCliente, razonSocial, numeroContacto, rubro, correo,  contrasena, salida])
    return salida.getvalue()

def listar_rubro():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama 
    out_cur = django_cursor.connection.cursor() #recibe
    cursor.callproc("SP_RUBRO",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listar_tipo_actividad():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama 
    out_cur = django_cursor.connection.cursor() #recibe
    cursor.callproc("SP_TIPO_ACTIVIDAD",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista