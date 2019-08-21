def get_match_result(keywords, article):
    return {
        'title_match': any([keyword for keyword in keywords if keyword in article.title]),
        'body_matches': any([keyword for keyword in keywords if keyword in article.text])
    }
