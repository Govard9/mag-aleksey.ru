# Generated by Django 3.1.5 on 2021-03-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0036_remove_horoscope_created_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default=1, max_length=250, verbose_name='Описание страницы'),
            preserve_default=False,
        ),
    ]
