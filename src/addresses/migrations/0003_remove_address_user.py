# Generated by Django 2.0.9 on 2019-03-02 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20190302_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
    ]