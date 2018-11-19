from django.urls import path, re_path
from . import views

namespace = 'news'


urlpatterns = [
    re_path('^news/', views.NewsListView.as_view(), name='news-list'),
    re_path(r'^scrape/$', views.scrape_news, name='scrape'),
]