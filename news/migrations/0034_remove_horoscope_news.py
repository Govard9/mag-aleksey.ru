# Generated by Django 3.1.1 on 2020-12-27 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0033_auto_20201223_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horoscope',
            name='news',
        ),
    ]