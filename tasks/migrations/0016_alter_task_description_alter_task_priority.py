# Generated by Django 4.2.16 on 2024-10-26 00:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_alter_task_priority_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=200, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('M', 'Media'), ('A', 'Alta'), ('B', 'Baja')], default='B', max_length=1, verbose_name='Prioridad'),
        ),
    ]
