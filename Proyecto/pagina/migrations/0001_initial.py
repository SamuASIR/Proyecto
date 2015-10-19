# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('lugar', models.CharField(max_length=35)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=9)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
