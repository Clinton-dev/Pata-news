from flask import render_template, request, url_for, redirect
from app import app
from .request import get_news,get_articles, search_news

app.config['SECRET_KEY'] = '3097c0d809dad8d3923f0afdb79f0e92'

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title="Pata news"
    source = get_news()

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search', news_name=search_news))
    else:
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


@app.route('/search/<news_name>')
def search(news_name):
    """
    Display search results
    """
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)
