# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_entryashka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('entryashka', models.ForeignKey(to='api.Entryashka', to_field='id')),
                ('link', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
