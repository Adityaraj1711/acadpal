# Generated by Django 3.0.6 on 2020-08-01 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200802_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
