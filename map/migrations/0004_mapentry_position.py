# Generated by Django 2.0.3 on 2018-03-19 20:45

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20180317_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapentry',
            name='position',
            field=geoposition.fields.GeopositionField(default=(34, 78), max_length=42),
            preserve_default=False,
        ),
    ]
