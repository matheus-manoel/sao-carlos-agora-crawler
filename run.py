import requests
from datetime import date

from newsplease import NewsPlease
from bs4 import BeautifulSoup

from src import get_match_result, get_links_and_dates, filter_links_by_date

page = requests.get('https://www.saocarlosagora.com.br/ultimas-noticias/')
soup = BeautifulSoup(page.content, 'html.parser')

result = get_links_and_dates(soup)

print(result)
print(date.today())
print(filter_links_by_date(result))


'''
article = NewsPlease.from_url('https://www.saocarlosagora.com.br/policia/apos-bater-na-esposa-e-em-uma-crianca-de-9-anos-homem-e-agredido-por/117007/')
keywords = ['casa', 'bebida', 'bater']
result = get_match_result(keywords, article)
print(result)
'''
