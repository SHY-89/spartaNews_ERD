from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = '뉴스 크롤링이 가능합니다. naver, daum'
    
    def handle(self, *args, **kwargs):
        # url = "https://n.news.naver.com/mnews/article/002/0000000001"
        url = "https://news.naver.com/section/105"
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url,headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        news_list = soup.select(".sa_text_title._NLOG_IMPRESSION")
        for e, news in enumerate(news_list, 1):
            new_url = news.attrs["href"]
            news_data = requests.get(new_url,headers=headers)
            news_soup = BeautifulSoup(news_data.text, 'html.parser')
            title = news_soup.select_one(".media_end_head_headline")
            content = news_soup.select_one(".go_trans._article_content")
            print(title.text)
            print(content.text)
    