# Generated by Django 4.0.4 on 2022-11-05 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_order_braintree_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='username',
        ),
    ]
