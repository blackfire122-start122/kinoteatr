# Generated by Django 3.2.8 on 2021-12-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_alter_films_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='actors',
            field=models.ManyToManyField(default=None, null=True, to='films.Actor'),
        ),
        migrations.AlterField(
            model_name='films',
            name='country',
            field=models.ManyToManyField(default=None, null=True, to='films.Country_film'),
        ),
        migrations.AlterField(
            model_name='films',
            name='genres',
            field=models.ManyToManyField(default=None, null=True, to='films.Genre'),
        ),
        migrations.AlterField(
            model_name='films',
            name='typef',
            field=models.ManyToManyField(default=None, null=True, to='films.Type'),
        ),
    ]
