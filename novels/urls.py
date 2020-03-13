from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.novels),
    re_path(r'^chapter_list/(?P<novelNo>[0-9]+)/$', views.chapter_list),
    re_path(r'^chapter_list/(?P<novelNo>[0-9]+)/(?P<chapterIdx>[0-9]+)/$', views.chapter)
]
