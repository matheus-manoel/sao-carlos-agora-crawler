def get_match_result(keywords, article):
    return {
        'title_match': any([keyword for keyword in keywords if keyword in article.title]),
        'body_matches': any([keyword for keyword in keywords if keyword in article.text])
    }

def get_links_and_dates(soupfied_last_news):
    news_list = [titulo.get('href') for titulo in
                 soupfied_last_news.find_all('a', {'class': 'titulos'})]
    return news_list
