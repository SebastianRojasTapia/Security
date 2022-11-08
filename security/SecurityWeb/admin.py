from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import *

# Register your models here.
admin.site.register(Profesional)
admin.site.register(Usuario)
admin.site.register(PerfilUsuario)
admin.site.register(Permission)
admin.site.register(ContentType)