# Generated by Django 3.2.8 on 2021-12-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_auto_20211212_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='year',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
