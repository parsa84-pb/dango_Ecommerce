# Generated by Django 3.1.1 on 2021-03-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0013_product_is_comment_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_comment_open',
            field=models.BooleanField(default=True, verbose_name='باز بودن نظرات'),
        ),
    ]
