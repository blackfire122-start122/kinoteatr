# Generated by Django 3.2.8 on 2021-12-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0021_serias_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serias',
            name='comments',
        ),
        migrations.AddField(
            model_name='serials',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='films.Comments'),
        ),
    ]
