# Generated by Django 3.0.7 on 2021-12-24 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_dislike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='like',
            name='video',
        ),
        migrations.DeleteModel(
            name='Dislike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
