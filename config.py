import os

class Config:
   ARTICLE_URL='http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
   ARTICLE_SOURCE_URL='https://newsapi.org/v2/sources?category={}&apiKey={}'
   NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
   SECRET_KEY= os.environ.get('SECRET_KEY')
   
class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}