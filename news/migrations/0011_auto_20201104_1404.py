# Generated by Django 3.1.1 on 2020-11-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20201104_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.AlterUniqueTogether(
            name='news',
            unique_together={('title', 'slug')},
        ),
    ]
