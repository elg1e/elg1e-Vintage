# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-17 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200406_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='clothingType',
            field=models.CharField(choices=[('tops', 'tops'), ('shirts', 'shirts'), ('jumpers', 'jumpers'), ('jeans', 'jeans'), ('accessories', 'accessories')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('mens', 'mens'), ('womens', 'womens')], default='mens', max_length=50),
        ),
    ]