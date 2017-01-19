# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='beacon',
            unique_together=set([('uuid', 'major', 'minor')]),
        ),
    ]
