from unicodedata import category
from app import app
import urllib.request,json
from .models import news_source,article

News = news_source.NewsSource
Article = article.Article

api_key = app.config['NEWS_API_KEY']
sources_url = app.config['SOURCE_API_BASE_URL']
article_url = app.config['ARTICLE_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        source_articles_response = json.loads(get_news_data)

        sources_results = None

        if source_articles_response['sources']:
            news_results_list = source_articles_response['sources']
            sources_results = process_results(news_results_list)

    return sources_results

def process_results(source_list):
    '''
    Function  that processes the news source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain movie details

    Returns :
        sources_results: A list of news article articles objects
    '''
    sources_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')

        source_object = News(id,name,description,category)
        sources_results.append(source_object)

    return sources_results


def get_articles(id):
    get_source_articles_url = article_url.format(id,api_key)

    with urllib.request.urlopen(get_source_articles_url) as url:
        source_articles_data = url.read()
        source_articles_response = json.loads(source_articles_data)

        articles_results = None
        if source_articles_response['articles']:
            news_results_list = source_articles_response['articles']
            articles_results = process_articles(news_results_list)

    return articles_results

def process_articles(articles_list):
    """
    Function  that processes the news_articles result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain movie details

    Returns :
        article_results: A list of news article articles objects
    """
    sources_results = []
    for source_item in articles_list:
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        urlToImage = source_item.get('urlToImage')

        source_object = Article(title,description,url,urlToImage)
        sources_results.append(source_object)

    return sources_results

# search news articles
def search_news(query):
    search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(query,api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_articles(search_news_list)

    return search_news_results