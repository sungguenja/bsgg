# Generated by Django 3.1.4 on 2020-12-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamedata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='respon_time',
            field=models.IntegerField(default=0),
        ),
    ]
