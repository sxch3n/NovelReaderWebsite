from django import template
from novels.pydbc.mongodb import MongoDBNovel
from typing import List

register = template.Library()


@register.filter(name='get_chapter')
def get_chapter(chapter_link,base_url):
    mongodb = MongoDBNovel()
    mongodb.start_connection('chapters')
    cursor = mongodb.query({'link':base_url+chapter_link}, chapter_name=1, index=1, _id=0)
    if cursor:
        return cursor[0].get('chapter_name')
    else:
        return None


@register.filter(name='last_idx')
def get_last_idx(chapter_list: List):
    # returns index in the database, not the index in the list.
    # the chapter index in the database starts from 1,
    # since the 0-index is for the novel content page
    return len(chapter_list)
