# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_auto_20151022_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='web',
            field=models.URLField(max_length=100, null=True),
        ),
    ]
