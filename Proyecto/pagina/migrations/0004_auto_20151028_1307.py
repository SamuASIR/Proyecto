# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_hotel_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('fecha_entrada', models.DateTimeField()),
                ('fecha_salida', models.DateTimeField()),
                ('n_habitacion', models.CharField(max_length=50)),
                ('id_reserva', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=35)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.TextField()),
                ('pais', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='fecha',
        ),
    ]
