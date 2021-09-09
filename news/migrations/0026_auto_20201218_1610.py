# Generated by Django 3.1.1 on 2020-12-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0025_addreviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Ваш Email')),
                ('content', models.TextField(verbose_name='Сообщение')),
                ('created_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-created_add'],
            },
        ),
        migrations.DeleteModel(
            name='AddReviews',
        ),
    ]
