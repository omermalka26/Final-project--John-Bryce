import pymysql
from datetime import datetime, date
from database import db


class Vacation:
    @staticmethod
    def get_db_connection():
        return db.get_connection()

    @staticmethod
    def create_table():
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''CREATE TABLE IF NOT EXISTS vacations
                    (vacation_id INT AUTO_INCREMENT PRIMARY KEY,
                    country_id INT NOT NULL,
                    vacation_description TEXT NOT NULL,
                    vacation_start DATE NOT NULL,
                    vacation_end DATE NOT NULL,
                    price DECIMAL(10,2) NOT NULL,
                    picture_file_name VARCHAR(255) NOT NULL,
                    FOREIGN KEY (country_id) REFERENCES countries(country_id))
                '''
            cursor.execute(sql)
            connection.commit()
            cursor.close()
    
    @staticmethod
    def insert(country_id, vacation_description, vacation_start,
                                 vacation_end, price, picture_file_name):
        """
        Inserts a new vacation record into the database.
        Assumes all input data has been validated by the controller.
        """
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                sql = '''INSERT INTO vacations
                             (country_id, vacation_description, vacation_start,
                                vacation_end, price, picture_file_name)
                             VALUES(%s, %s, %s, %s, %s, %s)'''
                cursor.execute(sql, (country_id, vacation_description, vacation_start,
                                   vacation_end, price, picture_file_name))
                vacation_id = cursor.lastrowid
                connection.commit()
                cursor.close()
                return {'message': f"Vacation '{vacation_id}' inserted successfully", 'id': vacation_id}
            except pymysql.IntegrityError as e:
                cursor.close()
                return {'error': f"Database error: Could not insert vacation due to a constraint violation. Details: {e}"}
            except Exception as e:
                cursor.close()
                return {'error': f"An unexpected database error occurred during insertion: {e}"}
    @staticmethod
    def get_all():
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''
                SELECT v.*, COALESCE(l.likes_count, 0) as likes_count 
                FROM vacations v 
                LEFT JOIN (
                    SELECT vacation_id, COUNT(*) as likes_count 
                    FROM likes 
                    GROUP BY vacation_id
                ) l ON v.vacation_id = l.vacation_id 
                ORDER BY v.vacation_start ASC
            '''
            cursor.execute(sql)
            vacations = cursor.fetchall()
            cursor.close()
            return [dict(
                vacation_id=vacation['vacation_id'],
                country_id=vacation['country_id'],
                vacation_description=vacation['vacation_description'],
                vacation_start=vacation['vacation_start'],
                vacation_end=vacation['vacation_end'],
                price=vacation['price'],
                picture_file_name=vacation['picture_file_name'],
                likes_count=vacation['likes_count']
            ) for vacation in vacations]
    
    @staticmethod
    def get_by_id(vacation_id):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''
                SELECT v.*, COALESCE(l.likes_count, 0) as likes_count 
                FROM vacations v 
                LEFT JOIN (
                    SELECT vacation_id, COUNT(*) as likes_count 
                    FROM likes 
                    GROUP BY vacation_id
                ) l ON v.vacation_id = l.vacation_id 
                WHERE v.vacation_id = %s
            '''
            cursor.execute(sql, (vacation_id,))
            vacation = cursor.fetchone()
            cursor.close()
            if vacation:
                return dict(
                    vacation_id=vacation['vacation_id'],
                    country_id=vacation['country_id'],
                    vacation_description=vacation['vacation_description'],
                    vacation_start=vacation['vacation_start'],
                    vacation_end=vacation['vacation_end'],
                    price=vacation['price'],
                    picture_file_name=vacation['picture_file_name'],
                    likes_count=vacation['likes_count']
                )
            return None
    
    @staticmethod
    def update(vacation_id, **kwargs):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute('SELECT * FROM vacations WHERE vacation_id = %s', (vacation_id,))
                if not cursor.fetchone():
                    cursor.close()
                    return {'error': 'Vacation not found'}

                update_fields = []
                values = []
                for key, value in kwargs.items():
                    update_fields.append(f"{key} = %s")
                    values.append(value)
                
                if not update_fields:
                    cursor.close()
                    return {'error': 'No fields to update'}

                sql = f"UPDATE vacations SET {', '.join(update_fields)} WHERE vacation_id = %s"
                values.append(vacation_id)
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                return {'message': f"Vacation {vacation_id} updated successfully"}
            except pymysql.IntegrityError as e:
                cursor.close()
                return {'error': f"Database error: Could not update vacation due to a constraint violation. Details: {e}"}
            except Exception as e:
                cursor.close()
                return {'error': f"An unexpected database error occurred during update: {e}"}
    
    @staticmethod
    def delete(vacation_id):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM vacations WHERE vacation_id = %s', (vacation_id,))
            vacation = cursor.fetchone()
            if vacation is None:
                cursor.close()
                return None
            
            cursor.execute('DELETE FROM vacations WHERE vacation_id = %s', (vacation_id,))
            connection.commit()
            cursor.close()
            return {'message': f"Vacation {vacation_id} deleted successfully"}

    @staticmethod
    def get_user_liked_vacations(user_id):
        """Get list of vacation IDs that a user has liked"""
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = 'SELECT vacation_id FROM likes WHERE user_id = %s'
            cursor.execute(sql, (user_id,))
            liked_vacations = cursor.fetchall()
            cursor.close()
            return [row['vacation_id'] for row in liked_vacations]

    