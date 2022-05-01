from app import app
import urllib.request,json
from .models import news_source

News = news_source.NewsSource
api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        sources_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            sources_results = process_results(news_results_list)

    return sources_results

def process_results(news_list):
    '''
    Function  that processes the news article result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        sources_results: A list of news article sources objects
    '''
    sources_results = []
    for news_item in news_list:
        id = news_item.get('source')
        name = news_item.get('source')

        source_object = News(id['id'],name['name'])
        sources_results.append(source_object)

    return sources_results