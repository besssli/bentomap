# Generated by Django 2.0.9 on 2018-11-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodevent', '0004_delete_rental'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodevent',
            name='lat',
            field=models.FloatField(blank=True, default=121.539794),
        ),
        migrations.AddField(
            model_name='foodevent',
            name='lon',
            field=models.FloatField(blank=True, default=25.01735),
        ),
    ]