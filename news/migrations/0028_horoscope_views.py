# Generated by Django 3.1.1 on 2020-12-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0027_horoscope'),
    ]

    operations = [
        migrations.AddField(
            model_name='horoscope',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]
