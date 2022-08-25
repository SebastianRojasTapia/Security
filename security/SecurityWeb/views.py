# Create your views here.
from django.shortcuts import render
# adjuntamos la libreria de autenticar 
from django.contrib.auth import authenticate,logout,login as login_autent
#agregar decorador para impedir el ingreso a las paginas sin estar registrado
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
import cx_Oracle #para ocupar varibles de oracle

from datetime import datetime # libreria para saber la fecha actual

# Create your views here.


def index(request):
    return render(request,'index.html')