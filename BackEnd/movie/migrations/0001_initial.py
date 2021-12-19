# Generated by Django 3.0.7 on 2021-12-19 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(default='')),
                ('image', models.TextField()),
                ('video_file', models.TextField()),
                ('season_num', models.IntegerField()),
                ('show_start', models.DateField()),
            ],
        ),
    ]
