# interlinking_algorithm.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from article_service import ArticleService

class InterlinkingAlgorithm:
    def __init__(self, db_name, user, password, host="localhost", port="5432"):
        self.article_service = ArticleService(db_name, user, password, host, port)

    def compute_similarity(self, article, articles):
        """Compute the similarity between the given article and all other articles."""
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([article['content']] + [a['content'] for a in articles])
        cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
        return cosine_similarities

    def get_interlinks(self, article_id, num_links):
        """Get the most similar articles to the given article."""
        article = self.article_service.get_article(article_id)
        all_articles = self.article_service.get_all_articles()

        similarities = self.compute_similarity(article, all_articles)
        most_similar_article_indices = similarities.argsort()[:-num_links-1:-1]

        interlinks = [all_articles[i]['id'] for i in most_similar_article_indices]
        return interlinks

    def add_interlinks(self, article_id, num_links):
        """Add interlinks to the given article."""
        interlinks = self.get_interlinks(article_id, num_links)
        self.article_service.update_article_links(article_id, interlinks)

    def close_algorithm(self):
        """Close the database connection."""
        self.article_service.close_service()

# Usage:
# interlinking_algorithm = InterlinkingAlgorithm("my_database", "my_user", "my_password")
# interlinking_algorithm.add_interlinks("article_id", 6)
# interlinking_algorithm.close_algorithm()
