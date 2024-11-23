# Generated by Django 4.2.16 on 2024-11-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_alter_task_deadline_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(verbose_name='Fecha límite'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('B', 'Baja'), ('A', 'Alta'), ('M', 'Media')], default='B', max_length=1, verbose_name='Prioridad'),
        ),
    ]
