#!/usr/bin/env python3
"""
Complete database setup script
This script will create all tables and populate them with initial data
"""

import os
import shutil
from models.role import Role
from models.country import Country
from models.user import User
from models.vacation import Vacation
from models.like import Like
from werkzeug.security import generate_password_hash

def setup_database():
    """Complete database setup"""
    
    print("Starting database setup...")
    
    # 1. Create all tables
    print("Creating tables...")
    Role.create_table()
    Country.create_table()
    User.create_table()
    Vacation.create_table()
    Like.create_table()
    
    # 2. Insert roles
    print("Adding roles...")
    Role.insert("User")
    Role.insert("Admin")
    
    # 3. Insert countries
    print("Adding countries...")
    countries = [
        "Israel", "Italy", "United States", "Canada", "Spain",
        "China", "France", "United Kingdom", "India", "Japan",
        "Germany", "Australia", "Brazil", "Mexico", "South Africa",
        "Egypt", "Turkey", "Greece", "Netherlands", "Sweden"
    ]
    
    for country_name in countries:
        Country.insert(country_name)
    
    # 4. Insert admin user
    print("Adding admin user...")
    admin_data = {
        'email': "admin@admin.com",
        'password': "admin",
        'first_name': "Admin",
        'last_name': "User",
        'role_id': 2
    }
    
    existing_admin = User.get_by_email(admin_data['email'])
    if not existing_admin:
        User.insert(
            admin_data['first_name'],
            admin_data['last_name'],
            admin_data['email'],
            generate_password_hash(admin_data['password']),
            admin_data['role_id']
        )
    
    # 5. Insert vacations
    print("Adding vacations...")
    vacations = [
        (2, "Amazing vacation in Italy", "2025-09-01", "2025-09-07", 1500.00, "italy.jpg"),
        (5, "Beautiful beaches in Spain", "2025-09-15", "2025-09-22", 1200.00, "spain.jpg"),
        (10, "Adventure in Japan", "2025-10-01", "2025-10-08", 2000.00, "japan.jpg"),
        (7, "Relaxing in France", "2025-10-15", "2025-10-20", 1800.00, "france.jpg"),
        (3, "Explore USA", "2025-11-01", "2025-11-08", 1600.00, "usa.jpg"),
        (4, "Canadian wilderness", "2025-11-15", "2025-11-22", 1400.00, "canada.jpg"),
        (8, "UK cultural tour", "2025-12-01", "2025-12-08", 1700.00, "uk.jpg"),
        (11, "German Christmas markets", "2025-12-15", "2025-12-22", 1900.00, "germany.jpg"),
        (6, "Chinese New Year", "2026-01-01", "2026-01-08", 2200.00, "china.jpg"),
        (9, "Indian heritage tour", "2026-01-15", "2026-01-22", 1300.00, "india.jpg"),
        (12, "Australian outback", "2026-02-01", "2026-02-08", 2500.00, "australia.jpg"),
        (13, "Brazilian carnival", "2026-02-15", "2026-02-22", 2100.00, "brazil.jpg"),
        (14, "Mexican fiesta", "2026-03-01", "2026-03-08", 1400.00, "mexico.jpg"),
        (15, "South African safari", "2026-03-15", "2026-03-22", 2800.00, "safari.jpg"),
        (16, "Egyptian pyramids", "2026-04-01", "2026-04-08", 1800.00, "egypt.jpg"),
        (1, "Israel holy sites", "2026-04-15", "2026-04-22", 1600.00, "israel.jpg"),
        (17, "Turkish bazaars", "2026-05-01", "2026-05-08", 1500.00, "turkey.jpg"),
        (18, "Greek islands", "2026-05-15", "2026-05-22", 1700.00, "greece.jpg"),
        (19, "Dutch windmills", "2026-06-01", "2026-06-08", 1600.00, "netherlands.jpg"),
        (20, "Swedish aurora", "2026-06-15", "2026-06-22", 2400.00, "sweden.jpg")
    ]
    
    from database import db
    
    with db.get_db_connection() as connection:
        cursor = connection.cursor()
        
        for vacation in vacations:
            try:
                sql = '''INSERT INTO vacations
                         (country_id, vacation_description, vacation_start,
                            vacation_end, price, picture_file_name)
                         VALUES(%s, %s, %s, %s, %s, %s)'''
                cursor.execute(sql, vacation)
                print(f"Added vacation: {vacation[1]}")
            except Exception as e:
                print(f"Error adding vacation {vacation[1]}: {e}")
        
        connection.commit()
        cursor.close()
    
    # 6. Ensure all images exist
    print("Ensuring all images exist...")
    ensure_images()
    
    print("Database setup completed successfully!")
    print("Admin credentials: admin@admin.com / admin")

def ensure_images():
    """Ensure all required images exist by copying existing ones if needed"""
    
    image_mapping = {
        "germany.jpg": "france.jpg",
        "australia.jpg": "usa.jpg",
        "brazil.jpg": "mexico.jpg",
        "safari.jpg": "nigeria.jpg",
        "egypt.jpg": "israel.jpg",
        "turkey.jpg": "italy.jpg",
        "greece.jpg": "spain.jpg",
        "netherlands.jpg": "uk.jpg",
        "sweden.jpg": "canada.jpg"
    }
    
    images_dir = "images"
    
    for new_image, source_image in image_mapping.items():
        source_path = os.path.join(images_dir, source_image)
        dest_path = os.path.join(images_dir, new_image)
        
        if os.path.exists(source_path) and not os.path.exists(dest_path):
            shutil.copy2(source_path, dest_path)
            print(f"Created {new_image} from {source_image}")

if __name__ == "__main__":
    setup_database()
