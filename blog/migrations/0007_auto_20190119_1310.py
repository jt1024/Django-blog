# Generated by Django 2.1.3 on 2019-01-19 05:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190119_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 19, 5, 10, 31, 670855, tzinfo=utc)),
        ),
    ]