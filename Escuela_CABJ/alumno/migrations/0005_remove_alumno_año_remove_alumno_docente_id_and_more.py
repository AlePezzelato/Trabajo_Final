# Generated by Django 5.0.6 on 2024-05-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0004_alter_alumno_año_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='año',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='docente_id',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='materia_id',
        ),
        migrations.AddField(
            model_name='alumno',
            name='docente',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='alumno',
            name='materia',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
