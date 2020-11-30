# Views
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles

@main.route('/')
def index():
  general_news = get_sources('general')
  sports_news = get_sources('sport')
  technology_news = get_sources('technology')
  entertainment_news = get_sources('entertainment')
  science_news = get_sources('science')
  
  title = 'NewsApp - Welcome'
  return render_template('index.html',
                         title = title,
                         general = general_news,
                         sport = sports_news,
                         technology = technology_news,
                         entertainment = entertainment_news,
                         science = science_news)
  
  