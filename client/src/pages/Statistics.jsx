import React, { useState, useEffect } from 'react';
import { useUser } from '../contexts/UserContext.jsx';
import api from '../api/api.js';
import './Statistics.css';

const Statistics = () => {
  const { isAuthenticated, loading } = useUser();
  const [stats, setStats] = useState({
    vacations: null,
    users: null,
    likes: null,
    distribution: null
  });
  const [loadingStats, setLoadingStats] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (isAuthenticated && !loading) {
      fetchStatistics();
    }
  }, [isAuthenticated, loading]);

  const fetchStatistics = async () => {
    try {
      setLoadingStats(true);
      setError(null);

      // Fetch all statistics in parallel
      const [vacationsRes, usersRes, likesRes, distributionRes] = await Promise.all([
        api.statsAPI.getVacationsStats(),
        api.statsAPI.getUsersCount(),
        api.statsAPI.getLikesCount(),
        api.statsAPI.getLikesDistribution()
      ]);

      setStats({
        vacations: vacationsRes,
        users: usersRes,
        likes: likesRes,
        distribution: distributionRes
      });
    } catch (err) {
      console.error('Error fetching statistics:', err);
      setError('Failed to load statistics. Please try again.');
    } finally {
      setLoadingStats(false);
    }
  };

  if (loading) {
    return (
      <div className="statistics-container">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  if (!isAuthenticated) {
    return (
      <div className="statistics-container">
        <div className="error-message">
          <h2>🔒 Access Denied</h2>
          <p>You need to be logged in to view statistics.</p>
        </div>
      </div>
    );
  }

  if (loadingStats) {
    return (
      <div className="statistics-container">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading statistics...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="statistics-container">
        <div className="error-message">
          <h2>❌ Error</h2>
          <p>{error}</p>
          <button onClick={fetchStatistics} className="retry-btn">
            🔄 Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="statistics-container">
      <div className="statistics-header">
        <h1>📊 System Statistics</h1>
        <p>Real-time data from the vacation booking system</p>
      </div>

      <div className="stats-grid">
        {/* Vacations Statistics */}
        <div className="stat-card">
          <div className="stat-icon">🏖️</div>
          <h3>Vacations</h3>
          <div className="stat-details">
            <div className="stat-item">
              <span className="stat-label">Past:</span>
              <span className="stat-value">{stats.vacations?.past_vacations || 0}</span>
            </div>
            <div className="stat-item">
              <span className="stat-label">Ongoing:</span>
              <span className="stat-value ongoing">{stats.vacations?.on_going_vacations || 0}</span>
            </div>
            <div className="stat-item">
              <span className="stat-label">Future:</span>
              <span className="stat-value future">{stats.vacations?.future_vacations || 0}</span>
            </div>
          </div>
        </div>

        {/* Users Statistics */}
        <div className="stat-card">
          <div className="stat-icon">👥</div>
          <h3>Users</h3>
          <div className="stat-details">
            <div className="stat-item">
              <span className="stat-label">Total:</span>
              <span className="stat-value large">{stats.users?.total_users || 0}</span>
            </div>
          </div>
        </div>

        {/* Likes Statistics */}
        <div className="stat-card">
          <div className="stat-icon">❤️</div>
          <h3>Likes</h3>
          <div className="stat-details">
            <div className="stat-item">
              <span className="stat-label">Total:</span>
              <span className="stat-value large">{stats.likes?.total_likes || 0}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Likes Distribution */}
      {stats.distribution && stats.distribution.length > 0 && (
        <div className="distribution-section">
          <h2>🌟 Popular Destinations</h2>
          <div className="distribution-grid">
            {stats.distribution.map((item, index) => (
              <div key={index} className="distribution-card">
                <div className="destination-name">{item.destination}</div>
                <div className="likes-count">
                  <span className="likes-number">{item.likes}</span>
                  <span className="likes-label">likes</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="stats-footer">
        <p>Last updated: {new Date().toLocaleString()}</p>
        <button onClick={fetchStatistics} className="refresh-btn">
          🔄 Refresh Data
        </button>
      </div>
    </div>
  );
};

export default Statistics;

