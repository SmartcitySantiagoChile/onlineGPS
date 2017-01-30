from django.db import models

# Create your models here.
class Tramos15Min(models.Model):
    tramo = models.CharField(max_length=200)
    eje = models.CharField(max_length=200)
    hito_origen = models.CharField(max_length=200, blank=True, null=True)
    hito_destino = models.CharField(max_length=200, blank=True, null=True)
    zona = models.CharField(max_length=200, blank=True, null=True)
    destino = models.CharField(max_length=200, blank=True, null=True)
    calle_origen = models.CharField(max_length=200, blank=True, null=True)
    calle_destino = models.CharField(max_length=200, blank=True, null=True)
    dist_en_ruta = models.IntegerField()
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    velocidad_tramo = models.FloatField(blank=True, null=True)
    tiempo_viaje_tramo = models.IntegerField(blank=True, null=True)
    tiempo_viaje_eje = models.IntegerField(blank=True, null=True)
    velocidad_eje = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tramos_15min'
        unique_together = (('tramo', 'eje', 'dist_en_ruta'),)

class OrigenYDestinoEjes15Min(models.Model):
    eje = models.CharField(max_length=200, blank=True, null=True)
    hito_origen = models.CharField(max_length=200, blank=True, null=True)
    hito_destino = models.CharField(max_length=200, blank=True, null=True)
    zona = models.CharField(max_length=200, blank=True, null=True)
    destino = models.CharField(max_length=200, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'origen_y_destino_ejes_15_min'

