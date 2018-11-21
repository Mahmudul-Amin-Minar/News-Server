from django.urls import path, re_path

from . import views

namespace = 'news'


urlpatterns = [
    re_path('^news/', views.NewsListView.as_view(), name='news-list'),
    re_path('^filter/(?P<days>[0-9]+)/$', views.NewsListView.as_view(), name='filtered-list'),
    re_path('^scrape/$', views.scrape_news, name='scrape'),
    re_path('search/$', views.NewsSearch.as_view(), name='news-search'),

    path('archive/<int:year>/', views.NewsYearArchiveView.as_view(), name="news_year_archive"),
    path('archive/<int:year>/<int:month>/', views.NewsMonthArchiveView.as_view(month_format='%m'), name="news_month_archive"),
    path('archive/<int:year>/<int:month>/<int:day>/', views.NewsDayArchiveView.as_view(), name="news_day_archive"),
]