# Generated by Django 3.2.8 on 2021-12-17 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0022_auto_20211217_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='serials',
            name='typef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='films.type'),
        ),
    ]
