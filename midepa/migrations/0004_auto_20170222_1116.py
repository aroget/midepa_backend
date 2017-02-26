# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('midepa', '0003_auto_20170221_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='condominio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios', to='midepa.Condominio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='presupuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios', to='midepa.Presupuesto'),
        ),
    ]
