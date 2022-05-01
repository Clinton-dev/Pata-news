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
    source = get_news()
    return render_template('index.html', title= title, sources=source)

@app.route('/article/<article_id>')
def article(article_id):

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('article.html', id=article_id)