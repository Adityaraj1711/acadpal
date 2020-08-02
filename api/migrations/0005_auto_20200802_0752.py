# Generated by Django 3.0.6 on 2020-08-02 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200802_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='citypeople', to='api.City'),
        ),
        migrations.AddField(
            model_name='person',
            name='town',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='townpeople', to='api.Town'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]