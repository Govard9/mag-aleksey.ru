from django import template
from news.models import CategoryHoroscopes

register = template.Library()


@register.simple_tag(name='horoscope_ordering')
def get_horoscope_articles():
    return CategoryHoroscopes.objects.all().order_by('pk')[6:12]