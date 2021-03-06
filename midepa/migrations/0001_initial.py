# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 11:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=90)),
                ('apartments', models.PositiveIntegerField(default=0)),
                ('budget', models.PositiveIntegerField(default=0)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='midepa.Condominio')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('avatar', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=90)),
                ('last_name', models.CharField(max_length=90)),
                ('apartment_number', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('phone', models.CharField(blank=True, max_length=90, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('company_name', models.CharField(max_length=100)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios', to='midepa.Condominio')),
                ('presupuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios', to='midepa.Presupuesto')),
            ],
        ),
    ]
