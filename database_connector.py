# database_connector.py

import psycopg2
from psycopg2 import sql

class DatabaseConnector:
    def __init__(self, db_name, user, password, host="localhost", port="5432"):
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

    def fetch_articles(self):
        """Fetch all articles from the database."""
        self.cursor.execute("SELECT * FROM articles")
        return self.cursor.fetchall()

    def fetch_article(self, article_id):
        """Fetch a specific article from the database."""
        query = sql.SQL("SELECT * FROM articles WHERE id = {}").format(sql.Identifier(article_id))
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def update_article(self, article_id, interlinks):
        """Update an article in the database with new interlinks."""
        query = sql.SQL("UPDATE articles SET interlinks = {} WHERE id = {}").format(
            sql.Identifier(interlinks),
            sql.Identifier(article_id)
        )
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        """Close the database connection."""
        self.cursor.close()
        self.connection.close()

# Usage:
# db = DatabaseConnector("my_database", "my_user", "my_password")
# articles = db.fetch_articles()
# db.update_article("article_id", "new_interlinks")
# db.close_connection()
