# Generated by Django 3.0.8 on 2020-07-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commitment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitment',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]