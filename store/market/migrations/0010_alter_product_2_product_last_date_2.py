# Generated by Django 4.2 on 2023-08-12 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20230810_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_2',
            name='product_last_date_2',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 21, 21, 23, 103926)),
        ),
    ]
