import requests

from newsplease import NewsPlease
from bs4 import BeautifulSoup

from src import get_match_result, get_links_and_dates

page = requests.get('https://www.saocarlosagora.com.br/ultimas-noticias/')
soup = BeautifulSoup(page.content, 'html.parser')

result = get_links_and_dates(soup)

print(result)

'''
article = NewsPlease.from_url('https://www.saocarlosagora.com.br/policia/apos-bater-na-esposa-e-em-uma-crianca-de-9-anos-homem-e-agredido-por/117007/')
keywords = ['casa', 'bebida', 'bater']
result = get_match_result(keywords, article)
print(result)
'''
