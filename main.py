import datetime 
from rfeed import *
import requests
link="https://news.liverpool.ac.uk/category/press-release/"
articles_list = []
from bs4 import BeautifulSoup


def getArticleSummary(article_link,headline):
    r2 = requests.get(article_link)
    soup2 = BeautifulSoup(r2.text)
    i = 1
    publication_date = soup2.find('time')['datetime']
    data2 = soup2.findAll('p')[i]
    #For some reason the page likes to have random paragraphs which are empty?
    #So we set i=1 and increase it if there is more empty or near empty strings detected ie building names
    while(len(data2.text) < 30):
        i = i+1
        data2 = soup2.findAll('p')[i]
    article_pub_date = datetime.datetime.strptime(publication_date, "%Y-%m-%d %H:%M:%S")
    #append to articles_list in order to print as RSS compatible XML
    articles_list.append(Item(
        title = headline,
        link = article_link, 
        description = data2.text,
        guid = Guid(article_link),
        pubDate = datetime.datetime(article_pub_date.year, article_pub_date.month, article_pub_date.day, article_pub_date.hour, article_pub_date.minute)))

def getTitles(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text)
    if(r.status_code == 200):
        data = soup.findAll('a',attrs={'class':'news_post'})
        current = 0
        for headline in data:
            if(current % 2 == 1):
                #print(data[current].text)
                getArticleSummary(data[current].get('href'),data[current].text)
            elif current == 20:
                break
            current = current+1
getTitles(link)

feed = Feed(
    title = "News Liverpool RSS Feed",
    link = "http://www.example.com/rss",
    description = "News Aggregated from news.liverpool.ac.uk",
    language = "en-US",
    lastBuildDate = datetime.datetime.now(),
    items = articles_list)

print(feed.rss())
