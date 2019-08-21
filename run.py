from newsplease import NewsPlease

from src import get_match_result

article = NewsPlease.from_url('https://www.saocarlosagora.com.br/policia/apos-bater-na-esposa-e-em-uma-crianca-de-9-anos-homem-e-agredido-por/117007/')
keywords = ['casa', 'bebida', 'bater']
result = get_match_result(keywords, article)
print(result)
