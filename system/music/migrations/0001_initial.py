# Generated by Django 2.1 on 2018-12-22 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=250)),
                ('album_description', models.CharField(max_length=500)),
                ('album_genre', models.CharField(max_length=250)),
                ('publication_year', models.CharField(max_length=4)),
                ('album_url', models.CharField(max_length=1999)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=250)),
                ('file_type', models.CharField(max_length=10)),
                ('song_url', models.CharField(max_length=1999)),
            ],
        ),
    ]
