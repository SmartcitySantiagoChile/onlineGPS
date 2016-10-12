from django.db import models

# Create your models here.

class InfoParadas(models.Model):
    codigo = models.CharField(max_length=20, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    tiempo_ultimo_bus = models.DateTimeField(blank=True, null=True)
    subidas = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_paradas'

