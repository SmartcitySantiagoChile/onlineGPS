# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0003_detectordevice'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='device',
            field=models.ForeignKey(default=1, to='beacon.DetectorDevice'),
            preserve_default=False,
        ),
    ]
