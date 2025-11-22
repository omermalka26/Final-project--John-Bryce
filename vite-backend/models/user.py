import pymysql
from database import db

class User:
    @staticmethod
    def get_db_connection():
        return db.get_connection()

    @staticmethod
    def create_table():
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''CREATE TABLE IF NOT EXISTS users
                    (user_id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL,
                    role_id INT NOT NULL,
                    FOREIGN KEY (role_id) REFERENCES roles(role_id))
                '''
            cursor.execute(sql)
            connection.commit()
            cursor.close()
    
    @staticmethod
    def insert(first_name, last_name, email, password_hash, role_id):
        """
        Insert a new user with already hashed password
        """
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                sql = '''INSERT INTO users 
                        (first_name, last_name, email, password, role_id)
                        VALUES(%s, %s, %s, %s, %s)'''
                cursor.execute(sql, (first_name, last_name, email, password_hash, role_id))
                user_id = cursor.lastrowid
                connection.commit()
                cursor.close()
                return {
                    'user_id': user_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'role_id': role_id
                }
            except pymysql.IntegrityError:
                cursor.close()
                return None
    
    @staticmethod
    def get_all():
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = 'SELECT * FROM users'
            cursor.execute(sql)
            users = cursor.fetchall()
            cursor.close()
            return [dict(
                user_id=user['user_id'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                email=user['email'],
                role_id=user['role_id']
            ) for user in users]
    
    @staticmethod
    def get_by_id(user_id):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = 'SELECT * FROM users WHERE user_id = %s'
            cursor.execute(sql, (user_id,))
            user = cursor.fetchone()
            cursor.close()
            if user:
                return dict(
                    user_id=user['user_id'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                email=user['email'],
                role_id=user['role_id']
                )
            return None
    
    @staticmethod
    def get_by_email(email):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = 'SELECT * FROM users WHERE email = %s'
            cursor.execute(sql, (email,))
            user = cursor.fetchone()
            cursor.close()
            if user:
                return dict(
                    user_id=user['user_id'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                email=user['email'],
                password_hash=user['password'],
                role_id=user['role_id']
                )
            return None
    
    @staticmethod
    def update(user_id, **kwargs):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
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

                sql = f"UPDATE users SET {', '.join(update_fields)} WHERE user_id = %s"
                values.append(user_id)
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                return {'message': f"User {user_id} updated successfully"}
            except pymysql.IntegrityError:
                cursor.close()
                return None

    @staticmethod
    def delete(user_id):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
            user = cursor.fetchone()
            if user is None:
                cursor.close()
                return None
            
            cursor.execute('DELETE FROM users WHERE user_id = %s', (user_id,))
            connection.commit()
            cursor.close()
            return {'message': f"User {user_id} deleted successfully"}
