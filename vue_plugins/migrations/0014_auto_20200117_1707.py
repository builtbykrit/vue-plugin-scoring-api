# Generated by Django 2.2.4 on 2020-01-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue_plugins', '0013_auto_20191122_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='vueplugin',
            name='has_recent_downloads',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vueplugin',
            name='has_star_status',
            field=models.BooleanField(default=False),
        ),
    ]
