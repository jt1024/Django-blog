# Generated by Django 2.1.3 on 2019-01-19 05:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190119_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 19, 5, 15, 21, 863928, tzinfo=utc)),
        ),
    ]
