# Generated by Django 3.1.4 on 2020-12-23 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20201211_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealAmpli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=100)),
                ('damage_taken', models.FloatField(default=0)),
                ('damage_done', models.FloatField(default=0)),
                ('charac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
                ('weap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.weapon')),
            ],
        ),
    ]