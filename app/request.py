from unicodedata import category
from app import app
import urllib.request,json
from .models import news_source

News = news_source.NewsSource
api_key = app.config['NEWS_API_KEY']
sources_url = app.config['SOURCE_API_BASE_URL']
article_url = app.config['SOURCE_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        sources_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
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
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        category = news_item.get('category')

        source_object = News(id,name,description,category)
        sources_results.append(source_object)

    return sources_results


def get_articles(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object