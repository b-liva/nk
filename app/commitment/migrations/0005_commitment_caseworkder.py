# Generated by Django 3.0.8 on 2020-07-31 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caseworker', '0001_initial'),
        ('commitment', '0004_commitment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitment',
            name='caseworkder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='caseworker.CaseWorker'),
            preserve_default=False,
        ),
    ]
