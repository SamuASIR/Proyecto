# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_auto_20151028_1307'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
