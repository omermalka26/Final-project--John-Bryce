// Navbar.js - Main navigation menu
import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useUser } from '../contexts/UserContext.jsx';
import './Navbar.css';

const Navbar = () => {
  const { user, logout, isAuthenticated, isAdmin, loading } = useUser();
  const navigate = useNavigate();

  // Debug log
  console.log('Navbar - user:', user, 'isAuthenticated:', isAuthenticated, 'isAdmin:', isAdmin, 'loading:', loading);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-brand">
          🏖️ Vacation Booking
        </Link>
        
        <ul className="navbar-nav">
          <li className="nav-item">
            <Link to="/vacations" className="nav-link">
              Vacations
            </Link>
          </li>
          
          {isAuthenticated && (
            <li className="nav-item">
              <Link to="/statistics" className="nav-link">
                Statistics
              </Link>
            </li>
          )}
          
          <li className="nav-item">
            <Link to="/about" className="nav-link">
              About
            </Link>
          </li>
          
          {isAdmin && (
            <li className="nav-item">
              <Link to="/admin" className="nav-link">
                Admin
              </Link>
            </li>
          )}
        </ul>
        
        <div className="navbar-auth">
          {loading ? (
            <div className="loading-section">
              <span className="loading-text">Loading...</span>
            </div>
          ) : isAuthenticated ? (
            <div className="user-section">
              <span className="user-name">
                Hello, {user?.first_name} {user?.last_name}
              </span>
              <button onClick={handleLogout} className="logout-btn">
                Logout
              </button>
            </div>
          ) : (
            <div className="auth-buttons">
              <Link to="/login" className="nav-link">
                Login
              </Link>
              <Link to="/register" className="nav-link">
                Register
              </Link>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
