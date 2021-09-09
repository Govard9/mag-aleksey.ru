# Generated by Django 3.1.1 on 2020-12-23 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_auto_20201223_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryHoroscopes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Категория гороскопа')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Слаг категории')),
            ],
            options={
                'verbose_name': 'Категория гороскопа',
                'verbose_name_plural': 'Категории гороскопов',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='horoscope',
            name='category_horoscopes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='horoscopes', to='news.categoryhoroscopes', verbose_name='Месяц'),
            preserve_default=False,
        ),
    ]
