# Generated by Django 3.1.1 on 2020-12-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0007_remove_product_is_favorite'),
        ('eshop_favorite', '0002_auto_20201202_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteproductlist',
            name='product_list',
            field=models.ManyToManyField(blank=True, to='eshop_products.Product'),
        ),
    ]
