# Generated by Django 3.0.8 on 2020-07-23 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supporter', '0003_auto_20200723_2032'),
        ('case', '0003_remove_case_supporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='case.Case')),
                ('supporter', models.ManyToManyField(to='supporter.Supporter')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
