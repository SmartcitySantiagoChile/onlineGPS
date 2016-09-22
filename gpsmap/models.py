from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Gps(models.Model):
    patente = models.CharField(max_length=7, blank=True, null=True)
    servicio = models.CharField(max_length=50, blank=True, null=True)
    tiempo = models.DateTimeField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    fuera_de_ruta = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gps'


class UltimaCargaGps(models.Model):
    patente = models.CharField(max_length=8, blank=True, null=True)
    servicio = models.CharField(max_length=50, blank=True, null=True)
    tiempo = models.DateTimeField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ultima_carga_gps'

class UltimosGps(models.Model):
    patente = models.CharField(max_length=7, blank=True, null=True)
    servicio = models.CharField(max_length=51, blank=True, null=True)
    tiempo = models.DateTimeField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    fuera_de_ruta = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ultimos_gps'
