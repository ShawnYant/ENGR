# Generated by Django 4.0.4 on 2022-10-20 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_remove_restaurant_category_restaurant_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
