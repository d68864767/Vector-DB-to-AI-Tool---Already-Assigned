# optimize.py

import time
from interlinking_algorithm import InterlinkingAlgorithm
from database_connector import DatabaseConnector

class Optimizer:
    def __init__(self, db_name, user, password, host="localhost", port="5432"):
        self.interlinking_algorithm = InterlinkingAlgorithm(db_name, user, password, host, port)
        self.db = DatabaseConnector(db_name, user, password, host, port)

    def optimize_interlinking(self, num_links):
        """Optimize the interlinking process by adding interlinks to all articles in the database."""
        start_time = time.time()

        articles = self.db.fetch_articles()
        for article in articles:
            self.interlinking_algorithm.add_interlinks(article['id'], num_links)

        end_time = time.time()
        print(f"Interlinking optimization completed in {end_time - start_time} seconds.")

    def close_optimizer(self):
        """Close the database connection."""
        self.interlinking_algorithm.close_algorithm()
        self.db.close_connection()

# Usage:
# optimizer = Optimizer("my_database", "my_user", "my_password")
# optimizer.optimize_interlinking(6)
# optimizer.close_optimizer()
