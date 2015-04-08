from django import template
from asgard.utils import format_currency as f_c

register = template.Library()

@register.filter
def format_currency(value):
    return f_c(value)
