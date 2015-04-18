# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150404_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
    ]
