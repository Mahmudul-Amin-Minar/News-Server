from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import News
from .scraper import samakal


def scrape_news(request):
    url = "http://samakal.com/list/all"
    samakal(url)
    return redirect('/')


class NewsListView(ListView):
    model = News
    queryset = News.objects.all()
    template_name = 'news/news_list.html'
    context_object_name = 'news'
