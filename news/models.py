from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from pytils.translit import slugify


class News(models.Model):
     title = models.CharField(max_length=250, verbose_name='Наименование')
     content = models.TextField(blank=True, verbose_name='Контент')
     created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
     updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
     photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка статьи', blank=True)
     video = models.TextField(blank=True, verbose_name='Фрейм')
     is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
     category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, related_name='news') # on_delete=models.PROTECT - защита от удаления статей привязанных к категории.
     views = models.IntegerField(default=0, verbose_name='Просмотры')
     slug = models.SlugField(max_length=250, unique=True, verbose_name='Слаг статей')

     def get_absolute_url(self):
          return reverse('view_news', kwargs={"slug": self.slug})

     # Строковое представление объекта
     def __str__(self):
          return self.title

     def save(self, *args, **kwargs):
         value = self.title
         self.slug = slugify(value)
         super().save(*args, **kwargs)

     class Meta:
          verbose_name = 'Новость'
          verbose_name_plural = 'Новости'
          ordering = ['-created_ad']  # '-created_ad' - посты в обратном порядке. Свежие первые.


class Category(models.Model):
     title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование каегории')
     content = models.TextField(blank=True, verbose_name='Описание категории')
     slug = models.SlugField(max_length=150, unique=True, verbose_name='Слаг категорий')
     photo_category = models.ImageField(upload_to='photos_category/%Y/%m/%d/', verbose_name='Картинка категории', blank=True)

     def get_absolute_url(self):
          return reverse('category', kwargs={"slug": self.slug})

     def __str__(self):
          return self.title

     def save(self, *args, **kwargs):
         value = self.title
         self.slug = slugify(value)
         super().save(*args, **kwargs)

     class Meta:
          verbose_name = 'Категория'
          verbose_name_plural = 'Категории'
          ordering = ['title']


class Reviews(models.Model):
     name = models.CharField(max_length=150, verbose_name='Ваше имя')
     email = models.EmailField(max_length=150, unique=True, verbose_name='Ваш Email')
     content = models.TextField(blank=False, verbose_name='Сообщение')
     created_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

     def get_absolute_url(self):
          return reverse('reviews')

     def __str__(self):
          return self.name

     class Meta:
          verbose_name = 'Отзыв'
          verbose_name_plural = 'Отзывы'
          ordering = ['-created_add']  # '-created_ad' - посты в обратном порядке. Свежие первые.


class Horoscope(models.Model):
     title = models.CharField(max_length=150, verbose_name='Заголовок гороскопа')
     content = models.TextField(blank=False, verbose_name='Текст гороскопа')
     photo = models.ImageField(upload_to='photos_horosсope/%Y/%m/%d/', verbose_name='Картинка гороскопа', blank=True)
     slug = models.SlugField(max_length=150, unique=True, verbose_name='Слаг гороскопа')
     views = models.IntegerField(default=0, verbose_name='Просмотры')
     category_horoscopes = models.ForeignKey('CategoryHoroscopes', verbose_name='Месяц', on_delete=models.PROTECT, related_name='horoscopes')  # on_delete=models.PROTECT - защита от удаления статей привязанных к категории.

     def get_absolute_url(self):
          return reverse('horoscope', kwargs={"slug": self.slug})

     def __str__(self):
          return self.title

     def save(self, *args, **kwargs):
         value = self.title
         self.slug = slugify(value)
         super().save(*args, **kwargs)

     class Meta:
          verbose_name = 'Гороскоп'
          verbose_name_plural = 'Гороскопы'
          ordering = ['-title']  # '-created_ad' - посты в обратном порядке. Свежие первые.


class CategoryHoroscopes(models.Model):
     title = models.CharField(max_length=150, db_index=True, verbose_name='Категория гороскопа')
     slug = models.SlugField(max_length=150, unique=True, verbose_name='Слаг категории')

     def get_absolute_url(self):
          return reverse('category-horoscopes', kwargs={"slug": self.slug})

     def __str__(self):
          return self.title

     def save(self, *args, **kwargs):
         value = self.title
         self.slug = slugify(value)
         super().save(*args, **kwargs)

     class Meta:
          verbose_name = 'Категория гороскопа'
          verbose_name_plural = 'Категории гороскопов'
          ordering = ['title']