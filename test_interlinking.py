# test_interlinking.py

import unittest
from interlinking_algorithm import InterlinkingAlgorithm

class TestInterlinkingAlgorithm(unittest.TestCase):
    def setUp(self):
        self.interlinking_algorithm = InterlinkingAlgorithm("test_database", "test_user", "test_password")

    def test_compute_similarity(self):
        article = {'content': 'This is a test article.'}
        articles = [{'content': 'This is another test article.'}, {'content': 'This is yet another test article.'}]
        similarities = self.interlinking_algorithm.compute_similarity(article, articles)
        self.assertEqual(len(similarities), len(articles))

    def test_get_interlinks(self):
        article_id = 'test_article_id'
        num_links = 2
        interlinks = self.interlinking_algorithm.get_interlinks(article_id, num_links)
        self.assertEqual(len(interlinks), num_links)

    def test_add_interlinks(self):
        article_id = 'test_article_id'
        num_links = 2
        self.interlinking_algorithm.add_interlinks(article_id, num_links)
        article = self.interlinking_algorithm.article_service.get_article(article_id)
        self.assertEqual(len(article['interlinks']), num_links)

    def tearDown(self):
        self.interlinking_algorithm.close_algorithm()

if __name__ == '__main__':
    unittest.main()
