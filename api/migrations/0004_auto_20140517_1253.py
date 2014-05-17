# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='link',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='chat',
            name='key',
        ),
        migrations.DeleteModel(
            name='Key',
        ),
    ]
