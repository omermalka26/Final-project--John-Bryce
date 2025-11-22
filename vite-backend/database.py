import os
import pymysql
from contextlib import contextmanager

class DatabaseConfig:
    def __init__(self):
        self.host = os.environ.get('MYSQL_HOST', 'localhost')
        self.port = int(os.environ.get('MYSQL_PORT', 3306))
        self.database = os.environ.get('MYSQL_DATABASE', 'vacationdb')
        self.user = os.environ.get('MYSQL_USER', 'vacationuser')
        self.password = os.environ.get('MYSQL_PASSWORD', 'vacationpass')
        
    def get_connection(self):
        """Get a MySQL database connection"""
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False
        )
    
    @contextmanager
    def get_db_connection(self):
        """Context manager for database connections"""
        connection = None
        try:
            connection = self.get_connection()
            yield connection
        except Exception as e:
            if connection:
                connection.rollback()
            raise e
        finally:
            if connection:
                connection.close()

# Global database instance
db = DatabaseConfig()




