# Generated by Django 3.0.8 on 2020-07-23 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('recipient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipient',
            name='illness',
        ),
        migrations.AddField(
            model_name='recipient',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipient',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
