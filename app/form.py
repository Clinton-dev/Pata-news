from flask import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import DataRequired

class SearchForm(FlaskForm):
    newsname = StringField('news_query', validators=[DataRequired()])
    submit = SubmitField('search')