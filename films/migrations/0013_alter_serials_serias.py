# Generated by Django 3.2.8 on 2021-12-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0012_alter_serials_serias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serials',
            name='serias',
            field=models.ManyToManyField(to='films.Sezons'),
        ),
    ]
