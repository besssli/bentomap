# Generated by Django 2.0.9 on 2018-12-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodevent', '0004_auto_20181228_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takefood',
            name='rating',
            field=models.IntegerField(default=-1),
        ),
    ]