# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='actividades',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('spa', models.CharField(max_length=10)),
                ('desayuno', models.CharField(max_length=10)),
                ('comida', models.CharField(max_length=10)),
                ('cena', models.CharField(max_length=10)),
            ],
        ),
    ]
