from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title="Pata news"
    general_news = get_news("general")
    business_news = get_news("business")
    sports_news = get_news("sports")
    health_news = get_news("health")
    return render_template('index.html', title= title, general=general_news, sports=sports_news, business=business_news, health=health_news)

@app.route('/article/<article_id>')
def article(article_id):

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('article.html', id=article_id)