# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0012_comentario_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
