# Generated by Django 3.2.6 on 2021-08-28 20:26

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tractor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tractor',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default='SRID=3857;POINT(0.0 0.0)', srid=4326),
        ),
    ]