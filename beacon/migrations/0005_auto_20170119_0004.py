# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0004_event_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detectordevice',
            name='beacons',
        ),
        migrations.AddField(
            model_name='beaconlog',
            name='device',
            field=models.ForeignKey(default=1, to='beacon.DetectorDevice'),
            preserve_default=False,
        ),
    ]
