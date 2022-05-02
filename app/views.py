from flask import render_template, request, url_for
from app import app
from .request import get_news,get_articles, search_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title="Pata news"
    source = get_news()
    return render_template('index.html', title= title, sources=source)

@app.route('/articles/<article_id>')
def article(article_id):

    '''
    View root page function that returns the index page and its data
    '''
    article = get_articles(article_id)
    title = 'Pata news'
    print(article)
    return render_template('articles.html', title=title, articles=article)


@app.route('/search')
def search(news_name):
    """
    Display search results
    """
    name_list = news_name.split(" ")
    name_format = "+".join(name_list)
    searched_news = search_news(name_format)
    title= f"search results for {news_name}"
    return render_template('search.html', news = searched_news)