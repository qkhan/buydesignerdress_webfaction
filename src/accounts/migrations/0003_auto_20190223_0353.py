# Generated by Django 2.0.9 on 2019-02-23 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_guestemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestemail',
            name='active',
        ),
        migrations.RemoveField(
            model_name='guestemail',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='guestemail',
            name='update',
        ),
    ]
