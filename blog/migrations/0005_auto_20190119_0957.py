# Generated by Django 2.1.3 on 2019-01-19 01:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190118_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 19, 1, 57, 46, 528038, tzinfo=utc)),
        ),
    ]
