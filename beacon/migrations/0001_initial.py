# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('macAddr', models.CharField(max_length=20)),
                ('uuid', models.UUIDField(editable=False)),
                ('major', models.CharField(max_length=10)),
                ('minor', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='BeaconLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('rssi', models.IntegerField()),
                ('measurePower', models.IntegerField()),
                ('beacon', models.ForeignKey(to='beacon.Beacon')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('event', models.TextField()),
            ],
        ),
    ]
