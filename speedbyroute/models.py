# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tramos15minAll(models.Model):
	servicio = models.CharField(max_length=20, blank=True, null=True)
	servicio_usuario = models.CharField(max_length=20, blank=True, null=True)
	tramo = models.IntegerField(blank=True, null=True)
	latitud = models.FloatField(blank=True, null=True)
	longitud = models.FloatField(blank=True, null=True)
	velocidad = models.IntegerField(blank=True, null=True)
	tiempo_viaje = models.IntegerField(blank=True, null=True)

	class Meta:
		managed=False
		db_table = 'tramos_15min_all'