from django import template

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_categories_list')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/categories_list.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
