import pymysql
from database import db

class Role:
    @staticmethod
    def get_db_connection():
        return db.get_connection()

    @staticmethod
    def create_table():
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''CREATE TABLE IF NOT EXISTS roles
                    (role_id INT AUTO_INCREMENT PRIMARY KEY,
                    role_name VARCHAR(50) NOT NULL UNIQUE)
                '''
            cursor.execute(sql)
            connection.commit()
            cursor.close()
    
    @staticmethod
    def insert(role_name):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                sql = '''INSERT INTO roles
                        (role_name)
                        VALUES(%s)'''
                cursor.execute(sql, (role_name,))
                connection.commit()
                cursor.close()
            except pymysql.IntegrityError:
                cursor.close()
                return None
    
    @staticmethod
    def get_all():
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = 'SELECT * FROM roles'
            cursor.execute(sql)
            roles = cursor.fetchall()
            cursor.close()
            return [dict(
                role_id=role['role_id'],
                role_name=role['role_name']
            ) for role in roles]
    
    @staticmethod
    def get_by_id(role_id):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = 'SELECT * FROM roles WHERE role_id = %s'
            cursor.execute(sql, (role_id,))
            role = cursor.fetchone()
            cursor.close()
            if role:
                return dict(
                role_id=role['role_id'],
                role_name=role['role_name']
                )
            return None
    
    @staticmethod
    def update(role_id, **kwargs):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
               
                cursor.execute('SELECT * FROM roles WHERE role_id = %s', (role_id,))
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

                sql = f"UPDATE roles SET {', '.join(update_fields)} WHERE role_id = %s"
                values.append(role_id)
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                return {'message': f"Role {role_id} updated successfully"}
            except pymysql.IntegrityError:
                cursor.close()
                return None
    
    @staticmethod
    def delete(role_id):
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM roles WHERE role_id = %s', (role_id,))
            user = cursor.fetchone()
            if user is None:
                cursor.close()
                return None
            
            cursor.execute('DELETE FROM roles WHERE role_id = %s', (role_id,))
            connection.commit()
            cursor.close()
            return {'message': f"Role {role_id} deleted successfully"}