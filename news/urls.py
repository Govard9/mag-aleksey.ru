from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

from news.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('about/', about, name='about'),
    path('payment/', payment, name='payment'),
    path('services/', services, name='services'),
    # path('register/', register, name='register'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    path('video-reviews/', video_reviews, name='video-reviews'),
    path('besplatnyj-privorot/', besplatnyj_privorot, name='besplatnyj-privorot'),
    path('reviews/', ReviewsPage.as_view(), name='reviews'),
    path('search/', search, name='search'),
    # Страница с кэшем   path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('articles/', HomeNews.as_view(), name='articles'),
    path('', ArticleListView.as_view(), name='home'),
    path('news/<slug>/', ArticleDetailView.as_view(), name='view_news'),
    path('category/<slug>/', NewsByCategory.as_view(), name='category'),
    path('horoscope/<slug>/', HoroscopeDetailView.as_view(), name='horoscope'),
    path('category-horoscopes/<slug>/', HoroscopeByCategory.as_view(), name='category-horoscopes'),
    path('horoscopes/', HoroscopePage.as_view(), name='horoscopes'),
    path('add-news/', CreateNews.as_view(), name='add_news'),
    path('add-reviews/', AddReviews.as_view(), name='add_reviews'),
]