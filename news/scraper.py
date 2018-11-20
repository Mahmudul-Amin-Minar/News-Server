import requests
from urllib import request as req
from bs4 import BeautifulSoup

from .models import News

requests.packages.urllib3.disable_warnings()


# samakal news data collection
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


# priyo news data collection
def priyo(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    news_list = soup.find_all('div', class_='pr-4 mc-10')

    for x in news_list:
        titles = x.find_all('h4')
        links = x.find_all('div', class_='article-image')
        tags = x.find_all('div', class_='article-description')

    for title, link, tag in zip(titles, links, tags):

        if News.objects.filter(title=title.text).exists():
            continue
        else:
            category_slug = tag.find('a').text
            new_news = News()
            new_news.source_name = 'প্রিয় সংবাদ'
            new_news.source_slug = 'Priyo'
            new_news.title = title.text
            new_news.link = "https://www.priyo.com" + str(link.find('a').get('href'))
            new_news.img_link = link.find('img')['src']
            new_news.category_slug = category_slug

            new_news.save()


# prothon alo news data collection
def palo(url):
    page = requests.get(url)
    news = BeautifulSoup(page.text, 'html.parser')

    for title, link, img, category in zip(news.find_all('h2', class_='title_holder'),
                                          news.find_all('a', attrs={'class': 'link_overlay'}),
                                          news.find_all('div', class_='image'),
                                          news.find_all('a', class_='category aitm')):

        if News.objects.filter(title=title.text).exists():
            continue
        else:
            category_slug = category.text
            new_news = News()
            new_news.source_name = 'প্রথম আলো'
            new_news.source_slug = 'ProthomAlo'
            new_news.title = title.text
            link2 = link.get('href')
            new_news.link = "https://www.prothomalo.com/" + str(link2)
            lnk = img.find('img')
            new_news.img_link = "http:" + str(lnk['src'])
            new_news.category_slug = category_slug

            new_news.save()


