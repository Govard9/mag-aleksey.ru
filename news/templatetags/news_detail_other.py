from django import template
from news.models import News

register = template.Library()


@register.simple_tag(name='other_articles')
def get_other_articles():
    return News.objects.filter(is_published=True).select_related('category').order_by('?')[:3]