# Generated by Django 2.0.5 on 2018-06-29 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_remove_category_prospect_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='prospect_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prospect_type', to='items.Prospect'),
            preserve_default=False,
        ),
    ]
