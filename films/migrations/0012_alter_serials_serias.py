# Generated by Django 3.2.8 on 2021-12-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0011_auto_20211212_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serials',
            name='serias',
            field=models.ManyToManyField(to='films.Films'),
        ),
    ]
