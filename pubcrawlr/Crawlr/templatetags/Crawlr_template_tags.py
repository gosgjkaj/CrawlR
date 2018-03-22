from django import template
from Crawlr.models import Category

register = template.Library()

@register.inclusion_tag('Crawlr/cats.html')
def get_category_list():
    return{'cats': Category.objects.all()}
