# article_service.py

from database_connector import DatabaseConnector

class ArticleService:
    def __init__(self, db_name, user, password, host="localhost", port="5432"):
        self.db = DatabaseConnector(db_name, user, password, host, port)

    def get_all_articles(self):
        """Fetch all articles from the database."""
        return self.db.fetch_articles()

    def get_article(self, article_id):
        """Fetch a specific article from the database."""
        return self.db.fetch_article(article_id)

    def update_article_links(self, article_id, interlinks):
        """Update an article in the database with new interlinks."""
        self.db.update_article(article_id, interlinks)

    def close_service(self):
        """Close the database connection."""
        self.db.close_connection()

# Usage:
# article_service = ArticleService("my_database", "my_user", "my_password")
# articles = article_service.get_all_articles()
# article_service.update_article_links("article_id", "new_interlinks")
# article_service.close_service()
