# Generated by Django 3.1.1 on 2021-03-21 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0012_auto_20210305_2244'),
        ('eshop_favorite', '0006_auto_20210321_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteproductlist',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول'),
        ),
    ]
