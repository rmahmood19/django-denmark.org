# Generated by Django 2.0.3 on 2018-04-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetupEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('date', models.DateField()),
                ('start_time', models.TimeField(help_text='Starts at')),
                ('end_time', models.TimeField(help_text='Finishes at')),
                ('venue', models.CharField(max_length=200)),
            ],
        ),
    ]