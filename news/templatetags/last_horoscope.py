from django import template
from news.models import Horoscope

register = template.Library()


@register.simple_tag()
def last_article():
    last_pages = Horoscope.objects.order_by("-pk")[0:1]
    return {
        'last_pages': last_pages,
    }