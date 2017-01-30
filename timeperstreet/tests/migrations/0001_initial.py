# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrigenYDestinoEjes15Min',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eje', models.CharField(max_length=200, null=True, blank=True)),
                ('hito_origen', models.CharField(max_length=200, null=True, blank=True)),
                ('hito_destino', models.CharField(max_length=200, null=True, blank=True)),
                ('zona', models.CharField(max_length=200, null=True, blank=True)),
                ('destino', models.CharField(max_length=200, null=True, blank=True)),
                ('nombre', models.CharField(max_length=200, null=True, blank=True)),
                ('latitud', models.FloatField(null=True, blank=True)),
                ('longitud', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'origen_y_destino_ejes_15_min',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tramos15Min',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tramo', models.CharField(max_length=200)),
                ('eje', models.CharField(max_length=200)),
                ('hito_origen', models.CharField(max_length=200, null=True, blank=True)),
                ('hito_destino', models.CharField(max_length=200, null=True, blank=True)),
                ('zona', models.CharField(max_length=200, null=True, blank=True)),
                ('destino', models.CharField(max_length=200, null=True, blank=True)),
                ('calle_origen', models.CharField(max_length=200, null=True, blank=True)),
                ('calle_destino', models.CharField(max_length=200, null=True, blank=True)),
                ('dist_en_ruta', models.IntegerField()),
                ('latitud', models.FloatField(null=True, blank=True)),
                ('longitud', models.FloatField(null=True, blank=True)),
                ('x', models.IntegerField(null=True, blank=True)),
                ('y', models.IntegerField(null=True, blank=True)),
                ('velocidad_tramo', models.FloatField(null=True, blank=True)),
                ('tiempo_viaje_tramo', models.IntegerField(null=True, blank=True)),
                ('tiempo_viaje_eje', models.IntegerField(null=True, blank=True)),
                ('velocidad_eje', models.FloatField(null=True, blank=True)),
                ('super_lento', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tramos_15min',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='tramos15min',
            unique_together=set([('tramo', 'eje', 'dist_en_ruta')]),
        ),
    ]
