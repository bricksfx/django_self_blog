# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150410_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
