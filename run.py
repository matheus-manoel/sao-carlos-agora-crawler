import requests
from datetime import date

from newsplease import NewsPlease
from bs4 import BeautifulSoup

from src import get_match_result, get_links_and_dates, filter_links_by_date, get_articles

page = requests.get('https://www.saocarlosagora.com.br/ultimas-noticias/')
soup = BeautifulSoup(page.content, 'html.parser')

links_and_dates = get_links_and_dates(soup)

articles = get_articles(filter_links_by_date(links_and_dates))
result = [{
    **{
        'url': article.url,
        'title': article.title,
        'text': article.text,
    },
   **get_match_result(['policia'], article)
} for article in articles]




'''
article = NewsPlease.from_url('https://www.saocarlosagora.com.br/policia/apos-bater-na-esposa-e-em-uma-crianca-de-9-anos-homem-e-agredido-por/117007/')
keywords = ['casa', 'bebida', 'bater']
print(article.__dict__)
'''
