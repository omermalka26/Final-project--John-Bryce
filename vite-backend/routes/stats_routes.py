from flask import Blueprint, jsonify
from models.user import User
from models.vacation import Vacation
from models.country import Country
from models.like import Like
from database import db
from decorators.auth_decorator import token_required
import pymysql
from datetime import datetime

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/vacations/stats', methods=['GET'])
@token_required
def get_vacations_stats():
    """Get vacations statistics: past, ongoing, and future vacations"""
    try:
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            current_date = datetime.now().strftime('%Y-%m-%d')
            
            # Get past vacations (end date < current date)
            cursor.execute('SELECT COUNT(*) FROM vacations WHERE vacation_end < %s', (current_date,))
            past_vacations = cursor.fetchone()['COUNT(*)']
            
            # Get ongoing vacations (start date <= current date <= end date)
            cursor.execute('SELECT COUNT(*) FROM vacations WHERE vacation_start <= %s AND vacation_end >= %s', (current_date, current_date))
            ongoing_vacations = cursor.fetchone()['COUNT(*)']
            
            # Get future vacations (start date > current date)
            cursor.execute('SELECT COUNT(*) FROM vacations WHERE vacation_start > %s', (current_date,))
            future_vacations = cursor.fetchone()['COUNT(*)']
            
            cursor.close()
            
            return jsonify({
                "past_vacations": past_vacations,
                "on_going_vacations": ongoing_vacations,
                "future_vacations": future_vacations
            })
            
    except Exception as e:
        return jsonify({'error': f'Failed to get vacation statistics: {str(e)}'}), 500

@stats_bp.route('/users/count', methods=['GET'])
@token_required
def get_users_count():
    """Get total number of users in the system"""
    try:
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM users')
            total_users = cursor.fetchone()['COUNT(*)']
            
            cursor.close()
            
            return jsonify({
                "total_users": total_users
            })
            
    except Exception as e:
        return jsonify({'error': f'Failed to get users count: {str(e)}'}), 500

@stats_bp.route('/likes/count', methods=['GET'])
@token_required
def get_likes_count():
    """Get total number of likes in the system"""
    try:
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM likes')
            total_likes = cursor.fetchone()['COUNT(*)']
            
            cursor.close()
            
            return jsonify({
                "total_likes": total_likes
            })
            
    except Exception as e:
        return jsonify({'error': f'Failed to get likes count: {str(e)}'}), 500

@stats_bp.route('/likes/distribution', methods=['GET'])
@token_required
def get_likes_distribution():
    """Get likes distribution by vacation destinations"""
    try:
        with db.get_db_connection() as connection:
            cursor = connection.cursor()
            
            # Get likes distribution by vacation destinations
            cursor.execute('''
                SELECT 
                    c.country_name as destination,
                    COUNT(l.vacation_id) as likes
                FROM countries c
                JOIN vacations v ON c.country_id = v.country_id
                LEFT JOIN likes l ON v.vacation_id = l.vacation_id
                GROUP BY c.country_id, c.country_name
                HAVING COUNT(l.vacation_id) > 0
                ORDER BY likes DESC
            ''')
            
            distribution = cursor.fetchall()
            
            cursor.close()
            
            return jsonify([
                {
                    "destination": row['destination'],
                    "likes": row['likes']
                }
                for row in distribution
            ])
            
    except Exception as e:
        return jsonify({'error': f'Failed to get likes distribution: {str(e)}'}), 500
