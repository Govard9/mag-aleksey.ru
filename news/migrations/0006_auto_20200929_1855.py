# Generated by Django 3.1.1 on 2020-09-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]
