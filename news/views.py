import datetime
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView, ArchiveIndexView

from .models import News
from .scraper import samakal
from .scraper import priyo


def scrape_news(request):
    url = "http://samakal.com/list/all"
    samakal(url)
    priyo("https://www.priyo.com/")
    return redirect('/')


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = News.objects.all()
        start_date = datetime.date.today()
        day = self.kwargs.get('days')
        if day:
            day = int(day)
            if day == 1:
                queryset = News.objects.filter(added__date=start_date)
            else:
                end_date = start_date - datetime.timedelta(day)
                queryset = News.objects.filter(added__range=(end_date, start_date))
        return queryset


class NewsYearArchiveView(YearArchiveView):
    queryset = News.objects.all()
    date_field = "added"
    make_object_list = True
    allow_future = True


class NewsMonthArchiveView(MonthArchiveView):
    queryset = News.objects.all()
    date_field = "added"
    allow_future = True


class NewsDayArchiveView(DayArchiveView):
    queryset = News.objects.all()
    date_field = "added"
    allow_future = True
    month_format = '%m'
    context_object_name = 'news'
    template_name = 'news/news_list.html'
