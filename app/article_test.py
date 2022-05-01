import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsSource class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_article = Article("Amputee wraps up marathon record quest",'BBC News',"https://aklsaj.com","https://adsjldsf/somefancyimage.jpg")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article,Article))


if __name__ == '__main__':
    unittest.main()