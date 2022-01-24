# Generated by Django 3.2.11 on 2022-01-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descripton', models.TextField()),
                ('technology', models.CharField(max_length=100)),
                ('image', models.FilePathField(path='images')),
            ],
        ),
    ]
