# Generated by Django 5.0.6 on 2024-05-31 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0007_remove_curso_año_remove_docente_año_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='año',
            field=models.IntegerField(null=True),
        ),
    ]
