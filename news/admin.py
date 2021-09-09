from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import News, Category, Horoscope, CategoryHoroscopes


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'category', 'created_ad', 'updated_at', 'views', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'slug', 'category', 'content', 'photo', 'video', 'get_photo', 'is_published', 'views', 'created_ad', 'updated_at') # метод добавления разделов в саму новость.
    readonly_fields = ('get_photo', 'created_ad', 'views', 'updated_at') # метод для показа какие поля не нужно редактировать, так как они заполняются автоматически.

    def get_photo(self, obj):  # Вывод мини картинки
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Картинка'


class CategoryAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Category
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ('id', 'title', 'content', 'get_photo_category')
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # Запятая обязательно, так как это кортеж из одного элемента.

    def get_photo_category(self, obj):  # Вывод мини картинки
        if obj.photo_category:
            return mark_safe(f'<img src="{obj.photo_category.url}" width="75">')
        else:
            return '-'

    get_photo_category.short_description = 'Картинка категории'


class HoroscopesAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Horoscope
        fields = '__all__'


class HoroscopeAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'views', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    fields = ('title', 'slug', 'category_horoscopes', 'content', 'photo', 'get_photo', 'views') # метод добавления разделов в саму новость.
    readonly_fields = ('get_photo', 'views') # метод для показа какие поля не нужно редактировать, так как они заполня.тся автоматически.

    def get_photo(self, obj):  # Вывод мини картинки
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Картинка'


class CategoryHoroscopesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # Запятая обязательно, так как это кортеж из одного элемента.
    ordering = ['id']


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Horoscope, HoroscopeAdmin)
admin.site.register(CategoryHoroscopes, CategoryHoroscopesAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
