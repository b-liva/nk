# Generated by Django 3.0.8 on 2020-08-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseworker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseworker',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
