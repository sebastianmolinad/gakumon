# Generated by Django 3.0.2 on 2020-01-12 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcial',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='taller',
            name='imagen',
        ),
    ]