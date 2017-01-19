# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0005_auto_20170119_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beacon',
            name='macAddr',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
