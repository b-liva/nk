# Generated by Django 3.0.8 on 2020-07-23 19:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_remove_case_supporter'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
