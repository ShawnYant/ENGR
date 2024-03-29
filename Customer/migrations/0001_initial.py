# Generated by Django 4.0.4 on 2022-11-13 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=1)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(default='123', max_length=100)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('nickname', models.CharField(max_length=50)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('address', models.CharField(default='', max_length=1000)),
                ('phoneNo', models.CharField(default='', max_length=1000)),
                ('birthdate', models.DateField(null=True)),
                ('status', models.IntegerField(default=1)),
                ('update_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.CharField(max_length=100)),
                ('secureNo', models.CharField(max_length=5)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('update_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]
