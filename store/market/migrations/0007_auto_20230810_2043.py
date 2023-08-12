# Generated by Django 3.2.20 on 2023-08-10 14:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_alter_product_2_product_last_date_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='busket',
            name='weight_busket',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_2',
            name='product_last_date_2',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 43, 55, 191603)),
        ),
        migrations.AddField(
            model_name='product_2',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.category'),
        ),
    ]