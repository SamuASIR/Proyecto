# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0007_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('opinion', models.TextField()),
                ('usuario', models.ForeignKey(to='pagina.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='foto',
            field=models.ImageField(null=True, upload_to='pagina/static/media'),
        ),
    ]
