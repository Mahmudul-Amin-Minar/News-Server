from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import News
from .scraper import samakal
from .scraper import priyo
from  .scraper import palo


def scrape_news(request):
    url = "http://samakal.com/list/all"
    samakal(url)
    priyo("https://www.priyo.com/")
    palo("https://www.prothomalo.com/home/featured")
    return redirect('/')


class NewsListView(ListView):
    model = News
    queryset = News.objects.all()
    template_name = 'news/news_list.html'
    context_object_name = 'news'
