# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0002_auto_20170111_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectorDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('externalId', models.CharField(unique=True, max_length=32)),
                ('beacons', models.ManyToManyField(to='beacon.Beacon')),
            ],
        ),
    ]
