# Generated by Django 2.0.6 on 2018-07-23 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon_runner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marathonrunner',
            name='citizenship',
            field=models.CharField(max_length=1024, verbose_name='Citizenship'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='city',
            field=models.CharField(max_length=1024, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='email',
            field=models.EmailField(max_length=1024, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='emergency_contact',
            field=models.CharField(max_length=1024, verbose_name='Emergency contact name'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='emergency_phone',
            field=models.CharField(max_length=32, verbose_name='Emergency contact phone'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='first_name',
            field=models.CharField(max_length=1024, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='is_prof',
            field=models.NullBooleanField(verbose_name='Is runner a professional sportsman'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='last_name',
            field=models.TextField(max_length=1024, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='running_club',
            field=models.CharField(max_length=1024, verbose_name='Running club'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='second_phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Second phone'),
        ),
        migrations.AlterField(
            model_name='marathonrunner',
            name='t_shirt_size',
            field=models.CharField(blank=True, max_length=8, verbose_name='T-shirt size'),
        ),
    ]