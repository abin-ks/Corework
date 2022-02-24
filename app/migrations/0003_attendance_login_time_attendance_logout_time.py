# Generated by Django 4.0.1 on 2022-02-22 05:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_trainer_task_submissiondate'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='login_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='logout_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
