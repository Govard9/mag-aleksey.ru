# Generated by Django 3.1.5 on 2021-02-09 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0034_remove_horoscope_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='horoscope',
            name='created_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
    ]