# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class UltimosGps(models.Model):
    patente = models.CharField(max_length=7, blank=True, null=True)
    servicio = models.CharField(max_length=50, blank=True, null=True)
    servicio_usuario = models.CharField(max_length=50, blank=True, null=True)
    tiempo = models.DateTimeField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    dist_en_ruta = models.IntegerField(blank=True, null=True)
    dist_a_ruta = models.IntegerField(blank=True, null=True)
    velocidad_instantanea = models.IntegerField(blank=True, null=True)
    velocidad_2gps = models.IntegerField(blank=True, null=True)
    velocidad_4gps = models.IntegerField(blank=True, null=True)
    operador = models.IntegerField(blank=True, null=True)
    orientacion = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=10, blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ultimos_gps'

