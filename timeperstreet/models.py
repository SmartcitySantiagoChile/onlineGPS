from django.db import models

# Create your models here.
class VelocityOfLast15Min(models.Model):
    eje = models.CharField(max_length=100, blank=True, null=True)
    tramo = models.CharField(max_length=100, blank=True, null=True)
    tiempo = models.DateTimeField(blank=True, null=True)
    velocidad = models.FloatField(blank=True, null=True)
    tiempo_viaje = models.FloatField(blank=True, null=True)
    nobservaciones = models.IntegerField(blank=True, null=True)
    dist_en_ruta = models.IntegerField(blank=True, null=True)
    dia = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'velocidad_ultima_15min'

class StreetSection15Min(models.Model):
    id = models.CharField(max_length=200)
    eje = models.CharField(max_length=100)
    dist_en_ruta = models.IntegerField()
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tramos_15min'
        unique_together = (('eje', 'id', 'dist_en_ruta'),)


