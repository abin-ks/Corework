# Generated by Django 4.0.1 on 2022-02-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_attendance_login_time_attendance_logout_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]