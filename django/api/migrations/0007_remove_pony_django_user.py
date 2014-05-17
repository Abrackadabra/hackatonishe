# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20140517_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pony',
            name='django_user',
        ),
    ]
