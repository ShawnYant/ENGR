# Generated by Django 4.0.4 on 2022-10-03 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_restaurant_alter_product_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='restaurant',
        ),
    ]