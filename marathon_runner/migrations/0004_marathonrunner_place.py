# Generated by Django 2.0.6 on 2018-07-30 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon_runner', '0003_auto_20180730_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='marathonrunner',
            name='place',
            field=models.IntegerField(blank=True, null=True, verbose_name='Current runner place'),
        ),
    ]
