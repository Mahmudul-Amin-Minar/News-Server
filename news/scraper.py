import requests
from urllib import request as req
from bs4 import BeautifulSoup

from .models import News

requests.packages.urllib3.disable_warnings()


def samakal(url):
    url = url
    html_doc = req.urlopen(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    news = soup.find('div', class_='col-md-8 col-sm-12 col-xs-12')

    for title, link, img in zip(news.find_all('h4', class_='heading'), news.find_all('a', class_="link-overlay"),
                                news.find_all('img', class_='media-object img-btm-r img-60')):

        if News.objects.filter(title=title.string).exists():
            continue
        else:
            category_slug = str(link['href'].split('/')[3])
            new_news = News()
            new_news.source_name = 'সমকাল'
            new_news.source_slug = 'samakal'
            new_news.title = title.string
            new_news.link = link['href']
            new_news.img_link = img['src']
            new_news.category_slug = category_slug

            if category_slug == 'politics':
                new_news.category_name = 'রাজনীতি'
            elif category_slug == 'international':
                new_news.category_name = 'আন্তর্জাতিক'
            elif category_slug == 'bangladesh':
                new_news.category_name = 'বাংলাদেশ'
            elif category_slug == 'economics':
                new_news.category_name = 'অর্থনীতি'
            elif category_slug == 'entertainment':
                new_news.category_name = 'বিনোদন'
            elif category_slug == 'sports':
                new_news.category_name = 'খেলা'
            elif category_slug == 'probas':
                new_news.category_name = 'প্রবাস'
            else:
                new_news.category_name = 'বিবিধ'

            new_news.save()
