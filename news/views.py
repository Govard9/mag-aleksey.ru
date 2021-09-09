from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Category, Reviews, Horoscope, CategoryHoroscopes
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm, FormReviews
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'news/404.html', status=404)


def about(request):
    return render(request, 'news/about.html')


def payment(request):
    return render(request, 'news/payment.html')


def services(request):
    return render(request, 'news/services.html')


def video_reviews(request):
    return render(request, 'news/video-reviews.html')


def besplatnyj_privorot(request):
    return render(request, 'news/besplatnyj-privorot.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message_contact = ''
            message_contact += f'Форма обратной связи с сайта mag-aleksey.ru\n'
            message_contact += f'Имя: {form.cleaned_data["name"]}\n'
            message_contact += f'Почта: {form.cleaned_data["email"]}\n'
            message_contact += f'Номер: {form.cleaned_data["number"]}\n'
            message_contact += f'Сообщение:\n'
            message_contact += f'{form.cleaned_data["content"]}'

            mail = send_mail(form.cleaned_data['subject'], message_contact, 'belo-mag@yandex.ru', ['belo-mag@yandex.ru'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Не верно заполнено одно из полей')
    else:
        form = ContactForm()
    return render(request, 'news/contacts.html', {"form": form})


def search(request):
    search_query = request.GET.get('search', '')

    if search_query:
        ser = News.objects.filter(title__icontains=search_query)
    else:
        ser = News.objects.all()[0:20]
    return render(request, 'news/search.html', {"ser": ser})


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    extra_context = {'title': 'Статьи'}
    paginate_by = 20

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category') # .select_related('category') Убирает дублирование SQL запросов.


class ArticleListView(ListView):
    template_name = 'news/home_page.html'
    context_object_name = 'news'
    extra_context = {'title': 'Главная'}

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')[:5]


class ReviewsPage(ListView):
    template_name = 'news/reviews.html'
    context_object_name = 'review'
    extra_context = {'title': 'Отзывы'}
    paginate_by = 10

    def get_queryset(self):
        return Reviews.objects.all()


class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        # попытаться получить категорию
        category = get_object_or_404(Category, slug__iexact=self.kwargs.get('slug'))
        # вывести новости из категории
        queryset = category.news.all()
        return queryset


class ArticleDetailView(DetailView):
    model = News
    context_object_name = 'news_item'

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class HoroscopeDetailView(DetailView):
    model = Horoscope
    context_object_name = 'horoscopes_items'

    def get_queryset(self):
        return Horoscope.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class HoroscopeByCategory(DetailView):
    model = CategoryHoroscopes
    template_name = 'news/horoscope_list.html'
    context_object_name = 'category'


class HoroscopePage(ListView):
    template_name = 'news/horoscope.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return CategoryHoroscopes.objects.all().order_by('pk')[0:6]


class CreateNews(LoginRequiredMixin, CreateView):
    login_url = '/admin/login/' # Перенаправление в админку для авторизации
    form_class = NewsForm
    template_name = 'news/add_news.html'


class AddReviews(CreateView):
    form_class = FormReviews
    template_name = 'news/add_reviews.html'

