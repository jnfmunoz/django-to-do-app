# Generated by Django 5.1.2 on 2024-10-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_priority_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('Completada', 'Completada'), ('En Progreso', 'En Progreso')], default='En Progreso', max_length=12, verbose_name='Estado'),
        ),
    ]
