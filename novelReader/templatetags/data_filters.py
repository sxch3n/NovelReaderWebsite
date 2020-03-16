from typing import Dict

from django import template

register = template.Library()


@register.filter(name='get_val')
def get_val_by_key(dictionary: Dict, key):
    return dictionary.get(key)


@register.filter(name='last_elem')
def get_last_element(lst):
    return lst[-1]
