import urllib.request, json
from .models import Article, News_Source

# gettin api key and article base url plus source url
api_key = None
base_url = None
source_url = None

def configure_request(app):
  global api_key, base_url, source_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['ARTICLE_API_BASE_URL']
  source_url = app.config['ARTICLE_SOURCE_URL']

def process_results(sources_list):
  sources_results = []
  for sources_item in sources_list:
    id = sources_item.get('id')
    name = sources_item.get('name')
    url = sources_item.get('url')
    category = sources_item.get('category')
    
    if id:
      sources_object = News_Source(id, name, url, category)
      sources_results.append(sources_object)
      
  return sources_results

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