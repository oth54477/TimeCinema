# Generated by Django 3.2.13 on 2022-11-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Era',
            fields=[
                ('era_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='era',
            field=models.ManyToManyField(related_name='era_movie', to='movies.Era'),
        ),
    ]
