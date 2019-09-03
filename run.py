import requests
from newsplease import NewsPlease
from bs4 import BeautifulSoup

from src import get_match_result, get_links_and_dates, filter_links_by_date, get_articles
from src.email_sender import send_email

page = requests.get('https://www.saocarlosagora.com.br/ultimas-noticias/')
soup = BeautifulSoup(page.content, 'html.parser')
emails_to_send = ['saocarlosagoracrawler@gmail.com']
keywords = ['copa', 'polícia']

links_and_dates = get_links_and_dates(soup)

articles = get_articles(filter_links_by_date(links_and_dates))
results = [{
    **{
        'url': article.url,
        'title': article.title,
    },
   **get_match_result(keywords, article)
} for article in articles]

message_html = '<p>Palavra(s)-chave: ' + ', '.join(keywords) + '</p>'
for result in results:
    if result['title_match'] or result['body_matches']:
        matches_to_display = ', '.join(list(set(result['title_match'] + result['body_matches'])))
        message_html += '<p><a href="' + result['url'] + '">' + result['title'] + '</a>'
        message_html += ' - Essa notícia pode te interessar pois contém a(s) seguinte(s) palavra(s)-chaves: ' + matches_to_display + '.</p>'

send_email(emails_to_send, message_html)
