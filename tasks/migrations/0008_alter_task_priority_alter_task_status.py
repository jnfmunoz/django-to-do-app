# Generated by Django 5.1.2 on 2024-10-20 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_priority_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('A', 'Alta'), ('B', 'Baja'), ('M', 'Media')], default='B', max_length=1, verbose_name='Prioridad'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('E', 'En Progreso'), ('C', 'Completada')], default='E', max_length=1, verbose_name='Estado'),
        ),
    ]
