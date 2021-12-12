# Generated by Django 3.2.8 on 2021-12-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0010_auto_20211212_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(default='', upload_to='video/')),
            ],
            options={
                'verbose_name': 'Seria',
                'verbose_name_plural': 'Serias',
            },
        ),
        migrations.AlterField(
            model_name='sezons',
            name='serias',
            field=models.ManyToManyField(to='films.Serias'),
        ),
    ]
