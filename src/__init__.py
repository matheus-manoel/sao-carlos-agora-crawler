from datetime import date

from newsplease import NewsPlease


def get_match_result(keywords, article):
    return {
        'title_match': [keyword for keyword in keywords if keyword in article.title],
        'body_matches': [keyword for keyword in keywords if keyword in article.text]
    }

def get_links_and_dates(soupfied_last_news):
    news_link_list = [titulo.get('href') for titulo in
                      soupfied_last_news.find_all('a', {'class': 'titulos'})]
    news_date_list = [lista_data.small.get_text() for lista_data in
                      soupfied_last_news.find_all('div', {'class': 'listaData'})]
    return dict(zip(news_link_list, news_date_list))

def _parse_date(raw_date, date=date):
    text_to_number = {
        'Jan': 1, 'Fev': 2, 'Mar': 3,
        'Abr': 4, 'Mai': 5, 'Jun': 6,
        'Jul': 7, 'Ago': 8, 'Set': 9,
        'Out': 10, 'Nov': 11, 'Dez': 12,
    }
    date_info = raw_date.split()
    return date(day=int(date_info[0]),
                month=text_to_number[date_info[1]],
                year=int(date_info[2]))

def filter_links_by_date(news_and_dates, date=date):
    return {
        k: v for k, v in news_and_dates.items()
        if _parse_date(v) == date.today()
    }

def get_articles(news_and_dates, np=NewsPlease):
    return [np.from_url(link) for link in news_and_dates]
