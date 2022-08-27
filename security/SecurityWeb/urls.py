from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('login/',login, name='LOG'),
    path('mision-vision/',visionMision, name='misionVision'),
    path('contacto/',contacto, name='contacto'),
    path('asesoria/',asesoria, name='asesoria'),
    path('plan/',plan, name='plan'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
]