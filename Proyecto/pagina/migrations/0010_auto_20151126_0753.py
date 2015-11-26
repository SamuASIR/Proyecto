# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0009_auto_20151125_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hotel',
            field=models.ForeignKey(to='pagina.hotel', default=1),
        ),
    ]
