# Generated by Django 5.0.6 on 2024-05-23 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumno', '0001_initial'),
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('codigo', models.CharField(max_length=30, unique=True)),
                ('alumnos', models.ManyToManyField(to='alumno.alumno')),
                ('docente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materias', to='docente.docente')),
            ],
        ),
    ]
