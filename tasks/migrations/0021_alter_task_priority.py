# Generated by Django 4.2.16 on 2024-11-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('B', 'Baja'), ('M', 'Media'), ('A', 'Alta')], default='B', max_length=1, verbose_name='Prioridad'),
        ),
    ]
