# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entryashka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('active_pony', models.ForeignKey(to='api.Pony', to_field='id')),
                ('passive_pony', models.ForeignKey(to='api.Pony', to_field='id')),
                ('torrent', models.ForeignKey(to='api.Torrent', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
