# Generated by Django 2.0.6 on 2018-07-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon_runner', '0002_auto_20180723_0317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marathonrunner',
            options={'verbose_name': 'Marathon runner', 'verbose_name_plural': 'Marathon runners'},
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='marathon_registration_datetime',
            field=models.DateTimeField(verbose_name='Marathon registration date and time'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='user_register_date',
            field=models.DateField(verbose_name='User registration date'),
        ),
    ]