# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actas_Administrativas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
                ('archivo', models.FileField(upload_to=b'archivos/categorias', null=True, verbose_name=b'Acta Administrativa', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('archivo', models.FileField(upload_to=b'archivos/categorias', null=True, verbose_name=b'Archivos', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_ingreso', models.DateField(null=True)),
                ('direccion', models.CharField(max_length=140, null=True)),
                ('curp', models.CharField(max_length=20, null=True)),
                ('rfc', models.CharField(max_length=20, null=True)),
                ('numero_seguridad_social', models.CharField(max_length=12, null=True)),
                ('celular', models.CharField(max_length=15, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
                ('edad', models.PositiveIntegerField(null=True)),
                ('estado_civil', models.CharField(max_length=150, null=True)),
                ('escolaridad', models.CharField(max_length=50, null=True)),
                ('preparacion_academica', models.CharField(max_length=140, null=True)),
                ('salario_contratacion', models.PositiveIntegerField(null=True)),
                ('salario_actual', models.PositiveIntegerField(null=True)),
                ('imagen', models.ImageField(default=b'images/empleado/default-01.png', upload_to=b'images/empleados', null=True, verbose_name=b'Imagen Empleado', blank=True)),
                ('departamento', models.ForeignKey(to='empleados.Departamento', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo_Vacaional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=80, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('fecha_inicio', models.DateField(null=True)),
                ('fecha_fin', models.DateField(null=True)),
                ('empleado', models.ForeignKey(to='empleados.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('perfil', models.TextField()),
                ('salario_minimo_inicial', models.PositiveIntegerField(null=True)),
                ('salario_maximo_inicial', models.PositiveIntegerField(null=True)),
                ('departamento', models.ForeignKey(to='empleados.Departamento', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(to='empleados.Puesto', null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='tipo_contrato',
            field=models.ForeignKey(to='empleados.Contrato', null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='archivo',
            name='empleado',
            field=models.ForeignKey(to='empleados.Empleado'),
        ),
        migrations.AddField(
            model_name='actas_administrativas',
            name='empleado',
            field=models.ForeignKey(to='empleados.Empleado'),
        ),
    ]
