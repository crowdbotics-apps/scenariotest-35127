# Generated by Django 2.2.26 on 2022-05-09 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220508_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='plan',
        ),
    ]
