# Generated by Django 3.1.1 on 2020-11-08 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20201108_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]