import os

class Config:
   ARTICLE_API_BASE_URL='http://newsapi.org/v2/top-headlines?country=gb&apiKey={}'
   ARTICLE_SOURCE_LINK='https://newsapi.org/v2/sources?category={}&apiKey={}'
   NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
   SECRET_KEY= os.environ.get('SECRETE_KEY')
   
class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}