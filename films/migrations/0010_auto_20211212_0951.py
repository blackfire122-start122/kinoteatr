# Generated by Django 3.2.8 on 2021-12-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0009_auto_20211212_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='serials',
            name='serias',
            field=models.ManyToManyField(to='films.Sezons'),
        ),
    ]