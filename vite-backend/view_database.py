#!/usr/bin/env python3
"""
Script to view database contents
"""

import sqlite3

def view_database():
    conn = sqlite3.connect('projectdb.db')
    cursor = conn.cursor()
    
    print("=== DATABASE OVERVIEW ===")
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"Tables: {[table[0] for table in tables]}")
    print()
    
    # View users
    print("=== USERS ===")
    cursor.execute("SELECT user_id, first_name, last_name, email, role_id FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]} {user[2]}, Email: {user[3]}, Role: {user[4]}")
    print()
    
    # View roles
    print("=== ROLES ===")
    cursor.execute("SELECT * FROM roles")
    roles = cursor.fetchall()
    for role in roles:
        print(f"ID: {role[0]}, Name: {role[1]}")
    print()
    
    # View countries
    print("=== COUNTRIES ===")
    cursor.execute("SELECT * FROM countries LIMIT 10")
    countries = cursor.fetchall()
    for country in countries:
        print(f"ID: {country[0]}, Name: {country[1]}")
    print(f"... and {len(countries)} more countries")
    print()
    
    # View vacations
    print("=== VACATIONS ===")
    cursor.execute("SELECT vacation_id, vacation_description, vacation_start, vacation_end, price FROM vacations LIMIT 5")
    vacations = cursor.fetchall()
    for vacation in vacations:
        print(f"ID: {vacation[0]}, Description: {vacation[1]}, Dates: {vacation[2]} to {vacation[3]}, Price: ${vacation[4]}")
    print(f"... and more vacations")
    print()
    
    # View likes
    print("=== LIKES ===")
    cursor.execute("SELECT COUNT(*) FROM likes")
    likes_count = cursor.fetchone()[0]
    print(f"Total likes: {likes_count}")
    
    if likes_count > 0:
        cursor.execute("SELECT user_id, vacation_id FROM likes LIMIT 5")
        likes = cursor.fetchall()
        for like in likes:
            print(f"User {like[0]} liked vacation {like[1]}")
    
    conn.close()

if __name__ == "__main__":
    view_database()






