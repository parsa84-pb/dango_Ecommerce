# Generated by Django 3.1.1 on 2020-12-03 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_favorite', '0003_auto_20201202_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoriteproductlist',
            old_name='product_list',
            new_name='list',
        ),
    ]
