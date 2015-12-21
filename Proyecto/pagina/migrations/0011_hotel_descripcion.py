# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0010_auto_20151126_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
