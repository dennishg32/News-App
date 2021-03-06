import urllib.request, json
from .models import Article, News_Source

# gettin api key and article base url plus source url
api_key = None
base_url = None
article_url = None

def configure_request(app):
  global api_key, base_url, article_url
  api_key=app.config['NEWS_API_KEY']
  base_url=app.config['ARTICLE_SOURCE_URL']
  article_url=app.config['ARTICLE_URL']

def get_sources(category):
  """ Function that gets the json response to our url request """
  
  get_sources_url = base_url.format(category, api_key)
  
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    
    source_results = None
    
    if get_sources_response['sources']:
      source_list = get_sources_response['sources']
      source_results = process_results(source_list)
  
  return source_results

def process_results(sources_list):
  sources_results = []
  for sources_item in sources_list:
    id = sources_item.get('id')
    name = sources_item.get('name')
    url = sources_item.get('url')
    category = sources_item.get('category')
    
    if id:
      sources_object = News_Source(id,name,url,category)
      sources_results.append(sources_object)
      
  return sources_results

def get_articles(id):
  get_articles_url = article_url.format(id, api_key)
  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)
    
    articles_res = None
    if get_articles_response['articles']:
      articles_list = get_articles_response['articles']
      articles_res = process_res(articles_list)
  
  return articles_res

def process_res(article_li):
  """ the use of dictionary so that we can see the list of objects"""
  
  articles_result = []
  dictionary = {}
  for article_item in article_li:
    
    source_id = article_item ['source']
    dictionary['id'] = source_id['id']
    dictionary['name'] = source_id['name']
    id = dictionary['id']
    name = dictionary['name']
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    url = article_item.get('url')
    urlToImage = article_item.get('urlToImage')
    publishedAt = article_item.get('publishedAt')
    
    if urlToImage:
      article_object = Article(id, name, author,title,description,url,urlToImage,publishedAt)
      articles_result.append(article_object)
  
  return articles_result