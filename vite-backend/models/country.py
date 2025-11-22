import pymysql
from database import db

class Country:
    @staticmethod
    def get_db_connection():
        return db.get_connection()

    @staticmethod
    def create_table():
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''CREATE TABLE IF NOT EXISTS countries
                    (country_id INT AUTO_INCREMENT PRIMARY KEY,
                    country_name VARCHAR(100) NOT NULL UNIQUE)
                '''
            cursor.execute(sql)
            connection.commit()
            cursor.close()
    
    @staticmethod
    def insert(country_name):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                sql = '''INSERT INTO countries 
                        (country_name)
                        VALUES(%s)'''
                cursor.execute(sql, (country_name,))
                country_id = cursor.lastrowid
                connection.commit()
                cursor.close()
                return {
                    'country_id': country_id,
                    'country_name': country_name
                }
            except pymysql.IntegrityError:
                cursor.close()
                return None
    
    @staticmethod
    def get_all():
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = 'SELECT * FROM countries'
            cursor.execute(sql)
            countries = cursor.fetchall()
            cursor.close()
            return [dict(
                country_id=country['country_id'],
                country_name=country['country_name']
            ) for country in countries]
    
    @staticmethod
    def get_by_id(country_id):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = 'SELECT * FROM countries WHERE country_id = %s'
            cursor.execute(sql, (country_id,))
            country = cursor.fetchone()
            cursor.close()
            if country:
                return dict(
                    country_id=country['country_id'],
                    country_name=country['country_name']
                )
            return None
    
    @staticmethod
    def update(country_id, **kwargs):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute('SELECT * FROM countries WHERE country_id = %s', (country_id,))
                if not cursor.fetchone():
                    cursor.close()
                    return None

                update_fields = []
                values = []
                for key, value in kwargs.items():
                    update_fields.append(f"{key} = %s")
                    values.append(value)
                
                if not update_fields:
                    cursor.close()
                    return None

                sql = f"UPDATE countries SET {', '.join(update_fields)} WHERE country_id = %s"
                values.append(country_id)
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                return {'message': f"Country {country_id} updated successfully"}
            except pymysql.IntegrityError:
                cursor.close()
                return None
    
    @staticmethod
    def delete(country_id):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM countries WHERE country_id = %s', (country_id,))
            country = cursor.fetchone()
            if country is None:
                cursor.close()
                return None
            
            cursor.execute('DELETE FROM countries WHERE country_id = %s', (country_id,))
            connection.commit()
            cursor.close()
            return {'message': f"Country {country_id} deleted successfully"}