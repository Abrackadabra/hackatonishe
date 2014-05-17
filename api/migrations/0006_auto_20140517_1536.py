# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_torrent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entryashka',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('active_pony', models.ForeignKey(to='api.Pony', to_field='id')),
                ('passive_pony', models.ForeignKey(to='api.Pony', to_field='id')),
                ('torrent', models.ForeignKey(to='api.Torrent', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pony',
            name='key',
            field=models.TextField(default='key'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='entryashka',
            field=models.ForeignKey(to='api.Entryashka', default=None, to_field='id'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='chat',
            name='talker',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='listener',
        ),
    ]
