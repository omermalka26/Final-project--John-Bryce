import React from 'react';
import './About.css';

const About = () => {
  return (
    <div className="about-container">
      <div className="about-header">
        <h1>👨‍💻 About the Developers</h1>
        <p>Meet the team behind the Vacation Booking System</p>
      </div>

      <div className="developers-section">
        <div className="developer-card">
          <div className="developer-avatar">
            <span className="avatar-icon">👨‍💻</span>
          </div>
          <div className="developer-info">
            <h3>Omer Malka</h3>
            <p className="developer-role">Full Stack Developer</p>
            <div className="developer-details">
              <p><strong>Email:</strong> omer.malka@example.com</p>
              <p><strong>GitHub:</strong> @omermalka26</p>
              <p><strong>Specialties:</strong> React, Node.js, Python, MySQL</p>
            </div>
            <div className="developer-skills">
              <span className="skill-tag">React</span>
              <span className="skill-tag">JavaScript</span>
              <span className="skill-tag">Python</span>
              <span className="skill-tag">Flask</span>
              <span className="skill-tag">MySQL</span>
              <span className="skill-tag">Docker</span>
            </div>
          </div>
        </div>

        <div className="developer-card">
          <div className="developer-avatar">
            <span className="avatar-icon">👨‍💻</span>
          </div>
          <div className="developer-info">
            <h3>Development Team</h3>
            <p className="developer-role">Software Engineers</p>
            <div className="developer-details">
              <p><strong>Focus:</strong> Full Stack Web Development</p>
              <p><strong>Experience:</strong> Modern Web Technologies</p>
              <p><strong>Passion:</strong> Creating User-Friendly Applications</p>
            </div>
            <div className="developer-skills">
              <span className="skill-tag">Frontend</span>
              <span className="skill-tag">Backend</span>
              <span className="skill-tag">Database</span>
              <span className="skill-tag">DevOps</span>
              <span className="skill-tag">UI/UX</span>
              <span className="skill-tag">API Design</span>
            </div>
          </div>
        </div>
      </div>

      <div className="project-section">
        <h2>🏖️ About the Project</h2>
        <div className="project-info">
          <div className="project-card">
            <div className="project-icon">🎯</div>
            <h3>Mission</h3>
            <p>To create a modern, user-friendly vacation booking system that makes travel planning simple and enjoyable for everyone.</p>
          </div>
          
          <div className="project-card">
            <div className="project-icon">🛠️</div>
            <h3>Technology Stack</h3>
            <p>Built with modern technologies including React, Flask, MySQL, and Docker for a scalable and maintainable solution.</p>
          </div>
          
          <div className="project-card">
            <div className="project-icon">🚀</div>
            <h3>Features</h3>
            <p>User authentication, vacation management, like system, statistics dashboard, and responsive design for all devices.</p>
          </div>
        </div>
      </div>

      <div className="tech-stack-section">
        <h2>💻 Technology Stack</h2>
        <div className="tech-grid">
          <div className="tech-category">
            <h3>Frontend</h3>
            <div className="tech-items">
              <span className="tech-item">React 18</span>
              <span className="tech-item">JavaScript ES6+</span>
              <span className="tech-item">CSS3</span>
              <span className="tech-item">React Router</span>
              <span className="tech-item">Context API</span>
            </div>
          </div>
          
          <div className="tech-category">
            <h3>Backend</h3>
            <div className="tech-items">
              <span className="tech-item">Python 3.11</span>
              <span className="tech-item">Flask</span>
              <span className="tech-item">PyMySQL</span>
              <span className="tech-item">JWT Authentication</span>
              <span className="tech-item">RESTful API</span>
            </div>
          </div>
          
          <div className="tech-category">
            <h3>Database</h3>
            <div className="tech-items">
              <span className="tech-item">MySQL 8.0</span>
              <span className="tech-item">Relational Design</span>
              <span className="tech-item">Foreign Keys</span>
              <span className="tech-item">Indexes</span>
            </div>
          </div>
          
          <div className="tech-category">
            <h3>DevOps</h3>
            <div className="tech-items">
              <span className="tech-item">Docker</span>
              <span className="tech-item">Docker Compose</span>
              <span className="tech-item">Containerization</span>
              <span className="tech-item">Multi-service</span>
            </div>
          </div>
        </div>
      </div>

      <div className="contact-section">
        <h2>📞 Contact Us</h2>
        <div className="contact-info">
          <div className="contact-item">
            <span className="contact-icon">📧</span>
            <span>Email: contact@vacationbooking.com</span>
          </div>
          <div className="contact-item">
            <span className="contact-icon">🌐</span>
            <span>Website: www.vacationbooking.com</span>
          </div>
          <div className="contact-item">
            <span className="contact-icon">📱</span>
            <span>Phone: +1 (555) 123-4567</span>
          </div>
        </div>
      </div>

      <div className="footer-note">
        <p>© 2024 Vacation Booking System. Built with ❤️ by the development team.</p>
      </div>
    </div>
  );
};

export default About;




