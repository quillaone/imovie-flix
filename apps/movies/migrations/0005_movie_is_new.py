# Generated by Django 4.1.3 on 2022-11-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_premier_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
