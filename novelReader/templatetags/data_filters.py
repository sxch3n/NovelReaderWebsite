from typing import Dict, List

from django import template

register = template.Library()


@register.filter(name='get_val')
def get_val_by_key(dictionary: Dict, key):
    return dictionary.get(key)


@register.filter(name='last_elem')
def get_last_element(list):
    return list[-1]

@register.filter(name='last_idx')
def get_last_idx(chapter_list: List):
    # returns index in the database, not the index in the list.
    # the chapter index in the database starts from 1,
    # since the 0-index is for the novel content page
    return len(chapter_list)

@register.filter(name='minus_one')
def minus_one(num:int):
    return num-1

@register.filter(name='add_one')
def add_one(num:int):
    return num+1