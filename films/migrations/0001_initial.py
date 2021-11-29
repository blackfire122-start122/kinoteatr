# Generated by Django 3.2.8 on 2021-11-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='actors/default.png', upload_to='actors/')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
            },
        ),
        migrations.CreateModel(
            name='Country_film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Country_film',
                'verbose_name_plural': 'Country_films',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img_film', models.ImageField(default='films/images/default.jpg', upload_to='film_img')),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('file', models.FileField(default='', upload_to='video/')),
                ('actors', models.ManyToManyField(to='films.Actor')),
                ('country', models.ManyToManyField(to='films.Country_film')),
                ('genres', models.ManyToManyField(to='films.Genre')),
                ('typef', models.ManyToManyField(to='films.Type')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
            },
        ),
    ]
