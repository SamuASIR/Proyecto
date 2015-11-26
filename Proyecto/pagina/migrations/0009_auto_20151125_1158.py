# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pagina', '0008_auto_20151119_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='id_reserva',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='n_habitacion',
        ),
        migrations.AddField(
            model_name='reserva',
            name='User',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hotel',
            field=models.OneToOneField(default=1, to='pagina.hotel'),
        ),
    ]
