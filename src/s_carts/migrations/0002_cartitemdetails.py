# Generated by Django 2.0.9 on 2019-06-15 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s_carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItemDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=0)),
                ('prd_qty', models.IntegerField(default=0)),
                ('prd_discount', models.IntegerField(default=0)),
                ('prd_total', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_carts.Cart')),
            ],
        ),
    ]
