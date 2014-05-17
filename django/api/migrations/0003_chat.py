# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_pony'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('talker', models.ForeignKey(to='api.Pony', to_field=u'id')),
                ('listener', models.ForeignKey(to='api.Pony', to_field=u'id')),
                ('key', models.OneToOneField(to='api.Key', to_field=u'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
