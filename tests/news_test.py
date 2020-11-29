import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
  ''' Test class to test the behaviour of the article '''
  def setUp(self):
    ''' set up method that will run before every test '''
    self.new_article = Article("Nexstar Media Wire","Second stimulus checks: Where we stand as November comes to a close - fox8.com","If you were betting political gridlock centered around the November election would come to an end after Americans went to the voting booth, you lost that bet.","https://fox8.com/news/second-stimulus-checks-where-we-stand-as-november-comes-to-a-close/","https://fox8.com/wp-content/uploads/sites/12/2020/11/GettyImages-1220795790-1-e1606680092313.jpg?w=1280","2020-11-29T20:00:00Z","** U.S. Rep. Tim Ryan talks about getting a stimulus bill passed back in September in the video above**\r\nWASHINGTON (NEXSTAR) — If you were betting political gridlock centered around the November ele… [+3784 chars]")
  
  def test_instance(self):
    self.assertEqual(isinstance(self.new_article))