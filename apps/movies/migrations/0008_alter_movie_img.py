# Generated by Django 4.1.3 on 2022-11-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_movie_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
