# Generated by Django 3.0.8 on 2020-08-08 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commitment', '0005_commitment_caseworkder'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitment',
            name='report_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='commitment',
            name='report_wanted',
            field=models.BooleanField(default=False),
        ),
    ]
