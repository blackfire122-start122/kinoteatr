# Generated by Django 3.2.8 on 2021-12-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211201_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(default='user_img/default.png', null=True, upload_to='user_img/'),
        ),
    ]
