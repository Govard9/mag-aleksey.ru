# Generated by Django 3.1.1 on 2020-11-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20201104_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Слаг'),
        ),
    ]
