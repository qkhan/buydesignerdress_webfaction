# Generated by Django 2.0.9 on 2019-03-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190223_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(default='normal', max_length=120),
            preserve_default=False,
        ),
    ]