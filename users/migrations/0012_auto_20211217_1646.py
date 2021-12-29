# Generated by Django 3.2.8 on 2021-12-17 14:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0025_auto_20211217_1646'),
        ('users', '0011_auto_20211217_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends_want_add',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='like_films',
            field=models.ManyToManyField(blank=True, to='films.Films'),
        ),
        migrations.AlterField(
            model_name='user',
            name='like_serials',
            field=models.ManyToManyField(blank=True, to='films.Serials'),
        ),
    ]
