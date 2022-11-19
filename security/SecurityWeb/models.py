# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime



class Actividad(models.Model):
    idactividad = models.BigAutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fechainicio = models.DateField(blank=True, null=True)  # This field type is a guess.
    fechatermino = models.DateField(blank=True, null=True)  # This field type is a guess.
    horainicio = models.TimeField(blank=True, null=True)  # This field type is a guess.
    horatermino = models.TimeField(blank=True, null=True)  # This field type is a guess.
    cantidadasistente = models.BigIntegerField(blank=True, null=True)
    fecharegistro = models.DateField(blank=True, null=True)  # This field type is a guess.
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    idtipoactividad = models.ForeignKey('TipoActividad', models.DO_NOTHING, db_column='idtipoactividad')
    rutcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='rutcliente')
    rutprofesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='rutprofesional',blank=True, null=True)
    idcheck = models.ForeignKey('CheckList', models.DO_NOTHING, db_column='idcheck', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad'


class CanalPago(models.Model):
    idcanalpago = models.BigAutoField(primary_key=True)
    descripcion = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'canal_pago'


class CheckList(models.Model):
    idcheck = models.BigAutoField(primary_key=True)
    isseniales = models.TextField(max_length=2, blank=True, null=True)
    iselementoseguridad = models.TextField(max_length=2, blank=True, null=True)
    ismaterial = models.TextField(max_length=2, blank=True, null=True)
    isredagua = models.TextField(max_length=2, blank=True, null=True)
    isluminaria = models.TextField(max_length=2, blank=True, null=True)
    isseguro = models.TextField(max_length=2, blank=True, null=True)
    istrabajoseguro = models.TextField(max_length=2, blank=True, null=True)
    descripcion = models.TextField(max_length=200)  # This field type is a guess.
    fecharegistro = models.DateField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'check_list'


class Cliente(models.Model):
    rutcliente = models.TextField(primary_key=True)  # This field type is a guess.
    razonsocial = models.TextField()  # This field type is a guess.
    numerocontacto = models.TextField(blank=True, null=True)  # This field type is a guess.
    ismoroso = models.CharField(max_length=1)
    idrubro = models.ForeignKey('Rubro', models.DO_NOTHING, db_column='idrubro')

    class Meta:
        managed = False
        db_table = 'cliente'


class ComprobantePago(models.Model):
    idcomprobante = models.BigAutoField(primary_key=True)
    numerotarjeta = models.TextField()  # This field type is a guess.
    pintarjeta = models.BigIntegerField()
    fechavalida = models.TextField()  # This field type is a guess.
    fecharegistro = models.DateField()  # This field type is a guess.
    monto = models.BigIntegerField()
    tipomoneda = models.TextField()  # This field type is a guess.
    valorusd = models.TextField()  # This field type is a guess.
    valoruf = models.TextField()  # This field type is a guess.
    valorutm = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'comprobante_pago'


class Contrato(models.Model):
    idcontrato = models.BigAutoField(primary_key=True)
    descripcion = models.TextField()  # This field type is a guess.
    vigente = models.CharField(max_length=1)
    valor = models.BigIntegerField()
    fechacontrato = models.DateTimeField()  # This field type is a guess.
    idpago = models.ForeignKey('Pago', models.DO_NOTHING, db_column='idpago')
    rutcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rutcliente')
    idactividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='idactividad')

    class Meta:
        managed = False
        db_table = 'contrato'


class HistorialActividad(models.Model):
    idhistorial = models.BigAutoField(primary_key=True)
    cantcapacitaciones = models.BigIntegerField(blank=True, null=True)
    cantaccidentesasistidos = models.BigIntegerField(blank=True, null=True)
    fecharegistro = models.DateField(blank=True, null=True)  # This field type is a guess.
    rutprofesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='rutprofesional')

    class Meta:
        managed = False
        db_table = 'historial_actividad'


class Pago(models.Model):
    idpago = models.BigAutoField(primary_key=True)
    fecharegistro = models.DateField()  # This field type is a guess.
    montopago = models.BigIntegerField()
    idcomprobante = models.ForeignKey(ComprobantePago, models.DO_NOTHING, db_column='idcomprobante')
    idcanalpago = models.ForeignKey(CanalPago, models.DO_NOTHING, db_column='idcanalpago')

    class Meta:
        managed = False
        db_table = 'pago'


class PerfilUsuario(models.Model):
    idperfil = models.BigAutoField(primary_key=True)
    descripcion = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'perfil_usuario'


class Profesional(models.Model):
    rutprofesional = models.TextField(primary_key=True)  # This field type is a guess.
    primernombre = models.TextField()  # This field type is a guess.
    segundonombre = models.TextField(blank=True, null=True)  # This field type is a guess.
    primerapellido = models.TextField()  # This field type is a guess.
    segundoapellido = models.TextField()  # This field type is a guess.
    numerocontacto = models.TextField()  # This field type is a guess.
    isvigente = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'profesional'


class Rubro(models.Model):
    idrubro = models.BigAutoField(primary_key=True)
    descripcion = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rubro'


class TipoActividad(models.Model):
    idtipoactividad = models.BigAutoField(primary_key=True)
    descripcion = models.TextField()  # This field type is a guess.
    montoactividad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_actividad'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    correo = models.TextField()  # This field type is a guess.
    contrasenahashed = models.TextField()  # This field type is a guess.
    ishabilitado = models.CharField(max_length=1)
    idperfil = models.ForeignKey(PerfilUsuario, models.DO_NOTHING, db_column='idperfil')
    rutcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rutcliente', blank=True, null=True)
    rutprofesional = models.ForeignKey(Profesional, models.DO_NOTHING, db_column='rutprofesional', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

# Create your models here.
class Room(models.Model):
    sala = models.CharField(max_length=1000,primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'room'


class Message(models.Model):
    idmessage = models.BigAutoField(primary_key=True)
    valor = models.CharField(max_length=1000000)
    datetime = models.DateField(blank=True)
    username = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    class Meta:
        managed = False
        db_table = 'message'