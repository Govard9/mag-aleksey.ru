from django import template
from news.models import News

register = template.Library()


@register.simple_tag(name='get_popular_news')
def get_news():
    return News.objects.filter(is_published=True).select_related('category').order_by('-views')[:5]