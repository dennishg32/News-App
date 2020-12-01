class Article:
  """
    definition of article objects
  """
  def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt):
    self.id = id
    self.name = name
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    

class News_Source:
  """ class to define a source objects """
  
  def __init__(self, id, name, url, category):
    self.id = id
    self.name = name
    self.url = url
    self.category = category
    