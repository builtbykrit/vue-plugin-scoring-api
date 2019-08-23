# Generated by Django 2.2.4 on 2019-08-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue_plugins', '0010_auto_20190823_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='vueplugin',
            name='repo_license_name',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AddField(
            model_name='vueplugin',
            name='repo_num_open_issues',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vueplugin',
            name='repo_readme',
            field=models.CharField(blank=True, max_length=131072),
        ),
    ]
