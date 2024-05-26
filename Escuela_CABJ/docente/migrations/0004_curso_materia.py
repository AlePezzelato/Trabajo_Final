# Generated by Django 5.0.6 on 2024-05-26 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0003_remove_docente_año_curso_docente_año'),
        ('materia', '0002_alter_materia_alumnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='materia',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='materia.materia'),
            preserve_default=False,
        ),
    ]
