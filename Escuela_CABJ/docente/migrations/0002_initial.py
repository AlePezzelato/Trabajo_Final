# Generated by Django 5.0.6 on 2024-05-23 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docente', '0001_initial'),
        ('materia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='materia_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='docentes', to='materia.materia'),
        ),
    ]
