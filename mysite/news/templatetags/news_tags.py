from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_categories_list')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/categories_list.html')
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {'categories': categories}

