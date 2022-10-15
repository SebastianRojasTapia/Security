# Create your views here.
from ast import For
from email.policy import strict
from http import client
from pydoc import describe
from re import U, template
from sqlite3 import Date
import string
from traceback import print_tb
from django.shortcuts import render
from django.contrib.auth.models import User
# adjuntamos la libreria de autenticar 
from django.contrib.auth import authenticate,logout,login as login_autent
#agregar decorador para impedir el ingreso a las paginas sin estar registrado
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection

import cx_Oracle #para ocupar varibles de oracle
import requests #llamados de api C#
import json

from datetime import date, datetime # libreria para saber la fecha actual


# Create your views here.

def logout_vista(request):
    logout(request)
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')


def contrato(request):
    return render(request,'contrato.html')

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
    user = request.user.get_username()
    dataMsg = {}
    if request.method == 'POST':
        url = "https://localhost:7000/ComprobantePago/SaveComprobante"

        numeroTarjeta = request.POST.get('numeroTarjeta')
        nombreTitular = request.POST.get('nombreTitular')
        mes = request.POST.get('mes')
        anio = request.POST.get('anio')
        fechaValida = mes+anio
        cvv = request.POST.get('cvv')
        monto = 60
        tipoMoneda = "CH"
        canalPago = 1
        descripcion = "Contratacion de Plan"

        headers = {'Content-Type': 'application/json'}

        payload = json.dumps({
            'numeroTarjeta':numeroTarjeta,
            'nombreTitular':nombreTitular,
            'fechaValida':fechaValida,
            'monto':monto,
            'tipoMoneda':tipoMoneda,
            'cvv':cvv
        })

        print(payload)
        
        response = requests.request("POST", url, headers=headers, data=payload, verify=False )

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))

            idcomprobante = data['idcomprobante']
            montoPago = data['montoPago']
            message = data['message']
            fechaRegistro = data['fechaRegistro']
            print(fechaRegistro)
            fechaRegistro = fechaRegistro.replace("T","")
            fechaRegistro = fechaRegistro[:-14]
            print(fechaRegistro)

            salida = SP_CONTRATO_PAGO(user,fechaRegistro,montoPago,canalPago,idcomprobante,descripcion)
            if salida == 1:
                dataMsg['mensaje'] = message
            else:
                dataMsg['mensaje'] = 'Error al contratar el plan'

    return render(request,'plan.html',dataMsg)

def visionMision(request):
    return render(request,'vision-mision.html')

def asesoria(request):
    return render(request,'asesoria.html')

def perfil(request):
    user = request.user.get_username()
    data = {'solicitud':listar_usuario(user)}
    if request.method == 'POST':
        correo = request.POST.get('email')
        telefono = request.POST.get('telefono')
        password = request.POST.get('password')
        password_confirmed= request.POST.get('password_confirmed')

        if password != None:
            if password == password_confirmed:
                print('hola cambiaste la clave')
                u = User.objects.get(username__exact=user)
                u.email = correo
                u.set_password(password)
                u.save()
                salida = SP_MODIFICAR_USER_PASS(telefono, correo, user, u.password)
                if salida == 1:
                    data['mensaje'] = 'Modificado correctamente'
                else:
                    data['mensaje'] = 'No se ha podido modificar'
            else:
                data['mensaje'] = 'Las contraseñas deben ser iguales'
        else:
            salida = SP_MODIFICAR_USER(telefono, correo, user)
             
            if salida == 1:
                data['mensaje'] = 'Modificado correctamente'
            else:
                data['mensaje'] = 'No se ha podido modificar'
    return render(request,'perfil.html',data)

#----------------- Listado -----------------
def agregar_usuario(rutCliente, razonSocial, numeroContacto,rubro,correo,contrasena):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_USUARIO_CLIENTE",[rutCliente, razonSocial, numeroContacto, rubro, correo,  contrasena, salida])
    return salida.getvalue()

def SP_MODIFICAR_USER_PASS(numeroContacto, correo, razonSocial, contrasena):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_USER_PASS",[numeroContacto, correo, razonSocial , contrasena, salida])
    return salida.getvalue()

def SP_MODIFICAR_USER(numeroContacto, correo, razonSocial):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_USER",[numeroContacto, correo, razonSocial, salida])
    return salida.getvalue()

def SP_CONTRATO_PAGO(razonSocial, fechaRegistro, montoPago, idCanalPago, idComprobantePago, descripcion):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_PAGO_CONTRATO",[razonSocial, fechaRegistro, montoPago, idCanalPago, idComprobantePago, descripcion, salida])
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

def listar_usuario(user):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama 
    out_cur = django_cursor.connection.cursor() #recibe
    cursor.callproc("SP_USUARIO",[user,out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)
        # print('\n'.join(map(str, lista)))
    return lista      