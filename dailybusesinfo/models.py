from django.db import models

# Create your models here.
class BusesDiarios(models.Model):
    servicio = models.CharField(max_length=50, primary_key=True)
    patente = models.CharField(max_length=7, primary_key=True)
    t_inicial = models.DateTimeField(primary_key=True)
    t_final = models.DateTimeField(blank=True, null=True)
    km_en_ruta = models.FloatField(blank=True, null=True)
    km_fuera_ruta = models.FloatField(blank=True, null=True)
    costo_en_ruta = models.FloatField(blank=True, null=True)
    costo_fuera_ruta = models.FloatField(blank=True, null=True)
    ultima_modificacion = models.DateTimeField(blank=True, null=True)
    t_en_ruta = models.DurationField(blank=True, null=True)
    t_fuera_ruta = models.DurationField(blank=True, null=True)
    velocidad_media = models.FloatField(blank=True, null=True)
    tipo_expedicion = models.IntegerField(blank=True, null=True)
    existe_ruta = models.IntegerField(blank=True, null=True)
    no_detenciones = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buses_diarios'
        unique_together = (('servicio', 'patente', 't_inicial'),)

