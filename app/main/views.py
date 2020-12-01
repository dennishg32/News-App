# Views
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles

@main.route('/')
def index():
  general_news = get_sources('general')
  technology_news = get_sources('technology')
  entertainment_news = get_sources('entertainment')
  
  title = 'NewsApp - Welcome'
  return render_template('index.html',
                         title = title,
                         general = general_news,
                         technology = technology_news,
                         entertainment = entertainment_news)
  
  
 
@main.route('/news/<id>')
def news(id):
  articles = get_articles(id)
  title = 'Welcome'
  return render_template('news.html', 
                         articles=articles,
                         title=title)
  
  