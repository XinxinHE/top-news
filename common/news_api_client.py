import requests

from json import loads


NEWS_API_ENDPOINT = 'https://newsapi.org/v1/'
NEWS_API_KEY = '3dc6460335914daea8a9b8ca306825f4'

ARTICLES_API = 'articles'

BBC_NEWS = 'bbc-news'
BBC_SPORT = 'bbc-sport'
CNN = 'cnn'

DEFAULT_SOURCES = [BBC_NEWS, CNN]
SORT_BY_TOP = 'top'

def buildUrl(endPoint=NEWS_API_ENDPOINT, apiName=ARTICLES_API):
    """ build the Url to fetch news """
    return endPoint + apiName

def getNewsFromSource(sources=DEFAULT_SOURCES, sortBy=SORT_BY_TOP):
    """ get news from source and save them into articles array """
    articles = []

    for source in sources:
        payload = {
            'apiKey': NEWS_API_KEY,
            'source': source,
            'sortBy': sortBy
        }

        response = requests.get(buildUrl(), params=payload)

        print response.content
        res_json = loads(response.content)

        # Extract info from response
        if (res_json is not None and
            res_json['status'] == 'ok' and
            res_json['source'] is not None):

            for news in res_json['articles']:
                news['source'] = res_json['source']
            
            articles.extend(res_json['articles'])

    return articles