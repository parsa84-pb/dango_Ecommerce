# Generated by Django 3.1.1 on 2020-11-23 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='about_us',
            field=models.TextField(blank=True, null=True, verbose_name='درباره ما'),
        ),
    ]
