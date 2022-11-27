from django.urls import path
from datetime import datetime
from .views import *
from . import views

time = datetime.now()
time = time.strftime("%m_%d_%Y_%H_%M_%S")
time = str(time)

urlpatterns = [
    path('',index, name='index'),
    path('login/',login, name='LOG'),
    path('login-profesional/',loginProfesional, name='LOGPROFE'),
    path('logout_vista/',logout_vista,name='LOGOUT'),

    path('mision-vision/',visionMision, name='misionVision'),
    path('contacto/',contacto, name='contacto'),
    path('asesoria/',asesoria, name='asesoria'),
    path('plan/',plan, name='plan'),

    path('perfil/',perfil, name='perfil'),
    path('perfil/plan/',perfil_cliente_plan, name='clientePlan'),

    path('perfil-Profesional/',perfil_profesional, name='perfilProfesional'),
    path('perfil-Profesional/kpi',perfil_profesional_kpi, name='perfilProfesionalKpi'),
    path('perfil-Profesional/kpi/Kpi_'+time, views.ViewPDF_KPI_Profesional.as_view(), name="pdf_kpi"),

    path('asesoria-cliente/',asesoriaCliente, name='asesoriaCliente'),

    path('check-index/',check_list_index,name='check_list_index'),
    path('check/<int:idcheck>/',check_list_modificar,name='check_modificar'),
    path('check/',check_list_modificar,name='check_modificar'),
    path('check-list/',checklist, name='check'),
    path('check-list/check_list_PDF_'+time, views.ViewPDF_Check_List.as_view(), name="pdf_view"),
    
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    
    path('contratar/',contratar, name='contratar'),
    path('contrato-cliente/',contratoCliente, name='contratoCliente'),
    
    path('actividad-index/',listado_actividad_profesional,name='listadoActividad'),
    path('asignarProfesional/<int:idactividad>/',asignarProfesional,name='asignarProfesional'),
    path('asignarProfesional/',asignarProfesional,name='asignarProfesional'),
    
    path('sala', home, name='home'),
    path('sala/<str:room>/', room, name='room'),
    path('listaChat/', listaChat, name='listaChat'),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),

    path('Vista/Extra/<int:extra_asesoria>/<int:extra_capacitacion>/', ViewPagoExtra, name='ViewPagoExtra'),
    path('pagoExtra', PagoExtra, name='PagoExtra'),
]