# Generated by Django 2.0.9 on 2018-12-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodevent', '0003_auto_20181228_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='name',
        ),
        migrations.AddField(
            model_name='place',
            name='place',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='foodevent',
            name='place',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]