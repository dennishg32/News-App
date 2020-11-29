import unittest
from app.models import News_Source

class News_SourceTest(unittest.TestCase):
   ''' Test class to test the behaviour of Sources of news'''
   def setUp(self):
     ''' set up method that will run before every test '''
     self.new_source = News_Source("axios","Axios", "The Gulf standoff has rumbled on for three years.","https://www.axios.com/kushner-visit-saudi-arabia-qatar-gulf-crisis-121cb422-ef27-4174-914c-ef8666972ab5.html","Sport news")
    
   def test_instance(self):
     self.assertEqual(isinstance(self.new_source))
     
  