from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('login/',login, name='LOG'),
    path('mision-vision/',visionMision, name='misionVision'),
    path('contacto/',contacto, name='contacto'),
    path('asesoria/',asesoria, name='asesoria'),
    path('perfil/',perfil, name='perfil'),
    path('plan/',plan, name='plan'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('contrato/',contrato,name='contrato'),
]