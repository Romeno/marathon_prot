# Generated by Django 2.0.6 on 2018-07-30 06:36

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marathon_common', '0003_auto_20180730_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='marathonroute',
            name='map',
            field=filebrowser.fields.FileBrowseField(default='', max_length=1024, verbose_name='GeoJSON of exported Yandex map'),
            preserve_default=False,
        ),
    ]
