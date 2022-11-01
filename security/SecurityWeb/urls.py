from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('login/',login, name='LOG'),
    path('mision-vision/',visionMision, name='misionVision'),
    path('contacto/',contacto, name='contacto'),
    path('asesoria/',asesoria, name='asesoria'),
    path('perfil/',perfil, name='perfil'),
    path('asesoria-cliente/',asesoriaCliente, name='asesoriaCliente'),
    path('check-list/',checklist, name='check'),
    path('plan/',plan, name='plan'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('contrato/',contrato,name='contrato'),
    path('check-index/',check_list_index,name='check_list_index'),
    path('check/<int:idcheck>/',check_list_modificar,name='check_modificar'),
    path('check/',check_list_modificar,name='check_modificar'),
    
]