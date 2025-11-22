#!/usr/bin/env python3
"""
Script to migrate data from SQLite to MySQL
"""

import sqlite3
import pymysql
from werkzeug.security import generate_password_hash
from database import db

def migrate_data():
    """Migrate all data from SQLite to MySQL"""
    
    print("Starting data migration from SQLite to MySQL...")
    
    # Connect to SQLite database
    sqlite_conn = sqlite3.connect('projectdb.db')
    sqlite_cursor = sqlite_conn.cursor()
    
    # Connect to MySQL database
    mysql_conn = db.get_connection()
    mysql_cursor = mysql_conn.cursor()
    
    try:
        # 1. Migrate roles
        print("Migrating roles...")
        sqlite_cursor.execute('SELECT * FROM roles')
        roles = sqlite_cursor.fetchall()
        
        for role in roles:
            role_id, role_name = role
            try:
                mysql_cursor.execute('INSERT INTO roles (role_id, role_name) VALUES (%s, %s)', (role_id, role_name))
                print(f"  Migrated role: {role_name}")
            except pymysql.IntegrityError:
                print(f"  Role {role_name} already exists, skipping...")
        
        # 2. Migrate countries
        print("Migrating countries...")
        sqlite_cursor.execute('SELECT * FROM countries')
        countries = sqlite_cursor.fetchall()
        
        for country in countries:
            country_id, country_name = country
            try:
                mysql_cursor.execute('INSERT INTO countries (country_id, country_name) VALUES (%s, %s)', (country_id, country_name))
                print(f"  Migrated country: {country_name}")
            except pymysql.IntegrityError:
                print(f"  Country {country_name} already exists, skipping...")
        
        # 3. Migrate users
        print("Migrating users...")
        sqlite_cursor.execute('SELECT * FROM users')
        users = sqlite_cursor.fetchall()
        
        for user in users:
            user_id, first_name, last_name, email, password, role_id = user
            try:
                # Check if password is already hashed
                if not password.startswith('scrypt:'):
                    password = generate_password_hash(password)
                
                mysql_cursor.execute('INSERT INTO users (user_id, first_name, last_name, email, password, role_id) VALUES (%s, %s, %s, %s, %s, %s)', 
                                   (user_id, first_name, last_name, email, password, role_id))
                print(f"  Migrated user: {first_name} {last_name} ({email})")
            except pymysql.IntegrityError:
                print(f"  User {email} already exists, skipping...")
        
        # 4. Migrate vacations
        print("Migrating vacations...")
        sqlite_cursor.execute('SELECT * FROM vacations')
        vacations = sqlite_cursor.fetchall()
        
        for vacation in vacations:
            vacation_id, country_id, vacation_description, vacation_start, vacation_end, price, picture_file_name = vacation
            try:
                mysql_cursor.execute('INSERT INTO vacations (vacation_id, country_id, vacation_description, vacation_start, vacation_end, price, picture_file_name) VALUES (%s, %s, %s, %s, %s, %s, %s)', 
                                   (vacation_id, country_id, vacation_description, vacation_start, vacation_end, price, picture_file_name))
                print(f"  Migrated vacation: {vacation_description}")
            except pymysql.IntegrityError:
                print(f"  Vacation {vacation_description} already exists, skipping...")
        
        # 5. Migrate likes
        print("Migrating likes...")
        sqlite_cursor.execute('SELECT * FROM likes')
        likes = sqlite_cursor.fetchall()
        
        for like in likes:
            user_id, vacation_id = like
            try:
                mysql_cursor.execute('INSERT INTO likes (user_id, vacation_id) VALUES (%s, %s)', (user_id, vacation_id))
                print(f"  Migrated like: User {user_id} liked vacation {vacation_id}")
            except pymysql.IntegrityError:
                print(f"  Like already exists, skipping...")
        
        # Commit all changes
        mysql_conn.commit()
        print("\n✅ Data migration completed successfully!")
        
        # Show summary
        mysql_cursor.execute('SELECT COUNT(*) FROM users')
        user_count = mysql_cursor.fetchone()['COUNT(*)']
        mysql_cursor.execute('SELECT COUNT(*) FROM vacations')
        vacation_count = mysql_cursor.fetchone()['COUNT(*)']
        mysql_cursor.execute('SELECT COUNT(*) FROM countries')
        country_count = mysql_cursor.fetchone()['COUNT(*)']
        mysql_cursor.execute('SELECT COUNT(*) FROM likes')
        like_count = mysql_cursor.fetchone()['COUNT(*)']
        
        print(f"\n📊 Migration Summary:")
        print(f"  Users: {user_count}")
        print(f"  Vacations: {vacation_count}")
        print(f"  Countries: {country_count}")
        print(f"  Likes: {like_count}")
        
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        mysql_conn.rollback()
    finally:
        sqlite_conn.close()
        mysql_cursor.close()
        mysql_conn.close()

if __name__ == "__main__":
    migrate_data()




