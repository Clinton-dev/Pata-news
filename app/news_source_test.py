import unittest
from models import news_source
Source = news_source.NewsSource

class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsSource class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_source = Source("bbc-news",'BBC News')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_source,Source))


if __name__ == '__main__':
    unittest.main()