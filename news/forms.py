from django import forms
from .models import News, Reviews
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField, CaptchaTextInput

from snowpenguin.django.recaptcha3.fields import ReCaptchaField


# Контактная форма
class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваш E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.IntegerField(label='Ваш номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
    captcha = ReCaptchaField()
    captcha2 = CaptchaField(label='Капча')


# Авторизация
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# Форма регистрации
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов.', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__' # все поля из модели
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        } # Подключение классов css


    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title


class FormReviews(forms.ModelForm):
    captcha = ReCaptchaField()
    captcha2 = CaptchaField(label='Капча')

    class Meta:
        model = Reviews
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        } # Подключение классов css

