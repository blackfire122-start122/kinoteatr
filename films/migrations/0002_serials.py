# Generated by Django 3.2.8 on 2021-12-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img_film', models.ImageField(default='films/images/default.jpg', upload_to='film_img')),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('actors', models.ManyToManyField(to='films.Actor')),
                ('country', models.ManyToManyField(to='films.Country_film')),
                ('genres', models.ManyToManyField(to='films.Genre')),
                ('serias', models.ManyToManyField(to='films.Films')),
            ],
            options={
                'verbose_name': 'Serial',
                'verbose_name_plural': 'Serials',
            },
        ),
    ]