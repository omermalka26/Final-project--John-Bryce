from flask import Flask, send_from_directory
from flask_cors import CORS
import os
import jwt
import time
from datetime import datetime, timedelta
from models.role import Role
from models.user import User
from models.country import Country
from models.vacation import Vacation
from models.like import Like
from routes.user_routes import user_bp
from routes.role_routes import role_bp
from routes.country_routes import country_bp
from routes.vacation_routes import vacation_bp
from routes.auth_routes import auth_bp
from routes.like_routes import like_bp
from routes.stats_routes import stats_bp

app = Flask(__name__)

# Enable CORS for React frontend (development and production)
CORS(app, supports_credentials=True, origins=[
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://localhost:5174", 
    "http://localhost:5175",
    "https://omermalka26.github.io",
    "https://*.onrender.com",
    "https://*.railway.app",
    "https://*.herokuapp.com"
])

# Serve static files (images)
IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

# Use environment variable for secret key (with fallback for development)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-super-secret-jwt-key-change-in-production')

# Register the blueprints
app.register_blueprint(user_bp)
app.register_blueprint(role_bp)
app.register_blueprint(country_bp)
app.register_blueprint(vacation_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(like_bp)
app.register_blueprint(stats_bp)

# Serve images
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGES_FOLDER, filename)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return {'error': 'Resource not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    return {'error': 'Internal server error'}, 500

def wait_for_mysql():
    """Wait for MySQL to be ready"""
    from database import db
    max_retries = 30
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            with db.get_db_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT 1")
                cursor.close()
            print("MySQL is ready!")
            return True
        except Exception as e:
            retry_count += 1
            print(f"Waiting for MySQL... (attempt {retry_count}/{max_retries})")
            time.sleep(2)
    
    print("Failed to connect to MySQL after maximum retries")
    return False

def create_tables():
    """Create database tables only"""
    try:
        print("Creating database tables...")
        Role.create_table()
        User.create_table()
        Country.create_table()
        Vacation.create_table()
        Like.create_table()
        print("Database tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")

# Removed populate_initial_data function - no automatic data insertion

# Wait for MySQL and create tables
if wait_for_mysql():
    create_tables()
else:
    print("Skipping table creation due to MySQL connection failure")

if __name__ == '__main__':
    # Get port from environment variable (for deployment) or use 5001 for vite-backend
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port) 

