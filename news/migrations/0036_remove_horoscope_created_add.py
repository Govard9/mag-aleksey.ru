# Generated by Django 3.1.5 on 2021-02-09 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0035_horoscope_created_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horoscope',
            name='created_add',
        ),
    ]