# Generated by Django 5.0.6 on 2024-05-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0007_alter_materia_año_materia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='docente',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
