# Generated by Django 3.2.8 on 2021-12-17 14:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0024_alter_serials_typef'),
        ('users', '0010_alter_user_friends_want_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_users_user_friends_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends_want_add',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='like_films',
            field=models.ManyToManyField(blank=True, null=True, to='films.Films'),
        ),
        migrations.AlterField(
            model_name='user',
            name='like_serials',
            field=models.ManyToManyField(blank=True, null=True, to='films.Serials'),
        ),
    ]