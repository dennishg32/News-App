import urllib.request, json
from .models import Article

# gettin api key and article base url plus source url
api_key = None
base_url = None
source_url = None

def configure_request(app):
  global api_key, base_url, source_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['ARTICLE_API_BASE_URL']
  source_url = app.config['ARTICLE_SOURCE_URL']


def get_sources(category):
  """ Function that gets the json response to our url request """

  get_sources_url = base_url.format(category, api_key)
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    
    source_results = None
    if get_sources_response['sources']:
      source_list = get_sources_response['sources']
      source_results = process_sources_results(source_list)
  
  return source_results