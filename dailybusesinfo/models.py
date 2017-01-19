from django.db import models

# Create your models here.
class BusesDiarios(models.Model):
    servicio = models.CharField(max_length=50, primary_key=True)
    patente = models.CharField(max_length=7, primary_key=True)
    km_en_ruta = models.FloatField(blank=True, null=True)
    km_fuera_ruta = models.FloatField(blank=True, null=True)
    costo_en_ruta = models.FloatField(blank=True, null=True)
    costo_fuera_ruta = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buses_diarios'
        unique_together = (('servicio', 'patente'),)

