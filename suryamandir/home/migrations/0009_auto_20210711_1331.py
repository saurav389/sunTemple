# Generated by Django 3.0.5 on 2021-07-11 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210711_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'ordering': ['-updated']},
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='timestamp',
        ),
    ]
