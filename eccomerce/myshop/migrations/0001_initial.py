# Generated by Django 3.2.6 on 2021-12-24 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
                ('product_category', models.CharField(max_length=25)),
                ('product_sub_category', models.CharField(max_length=15)),
                ('product_desc', models.CharField(max_length=75)),
                ('product_add_date', models.DateTimeField(auto_now_add=True)),
                ('product_manufact_date', models.DateField()),
                ('product_expiry_date', models.DateField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=25)),
                ('product_piece_left', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('check_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('product_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]