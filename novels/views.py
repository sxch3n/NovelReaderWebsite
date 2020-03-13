from django.shortcuts import render

from .pydbc.mongodb import MongoDBNovel


def novels(request):
    # TODO: 1. start spider to refresh the database.
    mongodb = MongoDBNovel()
    mongodb.start_connection(collection='novels')
    context = {'novels': [n for n in mongodb.query({})]}
    mongodb.close_connection()
    return render(request, 'novels.html', context)


def chapter_list(request, novelNo):
    # TODO: 2. combine with spider to scrape chapters every time user comes to the novel content page
    mongodb = MongoDBNovel()
    mongodb.start_connection(collection='novels')
    cursor = mongodb.query({'No': novelNo})
    mongodb.close_connection()
    if cursor:
        context = {'novel': cursor[0]}
        context['novel'].update({'base_link': 'https://{}'.format(context['novel']['link'].split('/')[2])})
    else:
        context = {'novel': {}}
    return render(request, 'chapter_list.html', context)


def chapter(request, novelNo, chapterIdx):
    mongodb = MongoDBNovel()
    mongodb.start_connection(collection='chapters')
    cursor = mongodb.query({'novel_no': novelNo, 'index': int(chapterIdx)})
    mongodb.close_connection()
    if cursor:
        context = {'chapter': cursor[0]}
        return render(request, 'chapter.html', context)
    else:
        return render(request, '404.html')
