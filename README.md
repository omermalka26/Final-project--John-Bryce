# 🏖️ Vacation Booking System

A full-stack web application for browsing, liking, and managing vacation packages with user authentication and admin capabilities.

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Environment Configuration](#-environment-configuration)
- [Running the Application](#-running-the-application)
- [Docker Deployment](#-docker-deployment)
- [API Documentation](#-api-documentation)
- [Database Schema](#-database-schema)
- [Authentication](#-authentication)
- [Usage](#-usage)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Features

### Core Functionality
- **User Authentication**: JWT-based login/registration system
- **Vacation Browsing**: View all available vacation packages with images
- **Like System**: Users can like/unlike vacations
- **Admin Dashboard**: Full CRUD operations for vacation management
- **Image Upload**: Secure file upload for vacation photos
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Ocean blue theme with glassmorphism effects

### Technical Features
- **Frontend**: React 18 with Vite for lightning-fast development
- **Backend**: Flask REST API with SQLite/MySQL database
- **Authentication**: JWT tokens with role-based access control
- **File Handling**: Secure image upload and serving
- **CORS**: Cross-origin resource sharing configuration
- **Containerization**: Docker support for easy deployment

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern JavaScript library
- **Vite** - Fast build tool and development server
- **React Router DOM** - Client-side routing
- **Context API** - State management
- **CSS3** - Modern styling with responsive design

### Backend
- **Flask** - Python web framework
- **SQLite/MySQL** - Database management
- **JWT** - JSON Web Token authentication
- **Werkzeug** - File upload handling
- **Pillow** - Image processing
- **bcrypt** - Password hashing

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

## 📁 Project Structure

```
Final-project--John-Bryce-/
├── client/                    # React frontend
│   ├── public/                # Static assets
│   ├── src/
│   │   ├── api/              # API communication
│   │   ├── components/       # Reusable React components
│   │   ├── contexts/         # React Context providers
│   │   ├── pages/            # Page components
│   │   └── main.jsx          # App entry point
│   ├── package.json
│   └── README.md
├── vite-backend/              # Flask backend
│   ├── controllers/           # Business logic
│   ├── models/               # Database models
│   ├── routes/               # API endpoints
│   ├── decorators/           # Authentication decorators
│   ├── images/               # Vacation images
│   ├── app.py               # Main Flask app
│   ├── requirements.txt
│   └── README.md
├── docker-compose.yml        # Docker orchestration
├── DOCKER_README.md          # Docker setup guide
└── README.md                # This file
```

## 📋 Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **Docker** (optional, for containerized deployment)
- **Git** for version control

## 🚀 Installation & Setup

### Option 1: Local Development Setup

#### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Final-project--John-Bryce-
```

#### 2. Backend Setup
```bash
# Navigate to backend directory
cd vite-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database (if needed)
python setup_database.py
```

#### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd ../client

# Install dependencies
npm install
```

### Option 2: Docker Setup

#### Using Docker Compose
```bash
# From project root directory
docker-compose up --build
```

This will start:
- MySQL database on port 3306
- Flask backend on port 5001
- React frontend on port 3000
- phpMyAdmin on port 8080

## 🔧 Environment Configuration

### Frontend Environment Variables
Create `.env` file in the `client/` directory:
```env
VITE_API_BASE_URL=http://localhost:5001
```

### Backend Environment Variables
Create `.env` file in the `vite-backend/` directory:
```env
SECRET_KEY=your-super-secret-jwt-key-change-in-production
FLASK_ENV=development
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=vacationdb
MYSQL_USER=vacationuser
MYSQL_PASSWORD=vacationpass
```

## 🏃 Running the Application

### Development Mode

#### Start Backend
```bash
cd vite-backend
python app.py
```
Backend will run on `http://localhost:5001`

#### Start Frontend
```bash
cd client
npm run dev
```
Frontend will run on `http://localhost:3000`

### Production Build

#### Frontend Production Build
```bash
cd client
npm run build
npm run preview  # To preview locally
```

## 🐳 Docker Deployment

### Quick Start with Docker Compose
```bash
# Build and run all services
docker-compose up --build

# Run in background
docker-compose up -d --build

# Stop services
docker-compose down

# View logs
docker-compose logs -f
```

### Individual Container Management
```bash
# Build specific service
docker-compose build backend
docker-compose build frontend

# Run specific service
docker-compose up backend
docker-compose up frontend
```

## 📚 API Documentation

### Authentication Endpoints
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user info

### Vacation Endpoints
- `GET /vacations` - Get all vacations
- `GET /vacations/:id` - Get specific vacation
- `POST /vacations` - Create vacation (admin only)
- `PUT /vacations/:id` - Update vacation (admin only)
- `DELETE /vacations/:id` - Delete vacation (admin only)
- `GET /vacations/user-likes` - Get user's liked vacations

### Other Endpoints
- `GET /countries` - Get all countries
- `POST /likes` - Add like to vacation
- `DELETE /likes` - Remove like from vacation
- `GET /images/<filename>` - Serve vacation images

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role_id INTEGER DEFAULT 2
);
```

### Vacations Table
```sql
CREATE TABLE vacations (
    vacation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vacation_description TEXT NOT NULL,
    country_id INTEGER NOT NULL,
    vacation_start DATE NOT NULL,
    vacation_end DATE NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    picture_file_name TEXT
);
```

### Countries Table
```sql
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT UNIQUE NOT NULL
);
```

### Likes Table
```sql
CREATE TABLE likes (
    like_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    vacation_id INTEGER NOT NULL,
    UNIQUE(user_id, vacation_id)
);
```

## 🔐 Authentication

### Default Admin User
- **Email**: admin@admin.com
- **Password**: admin

### JWT Token Structure
```json
{
  "user_id": 1,
  "email": "user@example.com",
  "role": "admin",
  "exp": 1234567890
}
```

### User Roles
- **Admin**: Full access to vacation management
- **User**: Can browse, like vacations, and view profiles

## 📱 Usage

### For Regular Users
1. **Register/Login**: Create account or login with existing credentials
2. **Browse Vacations**: View all available vacation packages
3. **Like Vacations**: Click heart icon to like/unlike vacations
4. **View Details**: See vacation descriptions, prices, and dates

### For Administrators
1. **Login** with admin credentials
2. **Access Admin Dashboard**: Click "Admin Dashboard" button
3. **Manage Vacations**: Add, edit, delete vacation packages
4. **Upload Images**: Add vacation photos during creation/editing
5. **View Statistics**: See like counts and user engagement

## 🧪 Testing

### Manual API Testing
```bash
# Login test
curl -X POST http://localhost:5001/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@admin.com","password":"admin"}'

# Get vacations
curl -X GET http://localhost:5001/vacations
```

### Frontend Testing
```bash
cd client
npm test  # If test scripts are configured
```

## 🚀 Deployment

### Frontend Deployment
Deploy the `client/dist` folder to:
- **Netlify**: Drag & drop dist folder
- **Vercel**: Connect GitHub repository
- **GitHub Pages**: Use gh-pages package

### Backend Deployment
Deploy to:
- **Heroku**: Use Procfile and requirements.txt
- **Railway**: Connect GitHub repository
- **DigitalOcean App Platform**: Docker-based deployment

### Production Considerations
- Set strong `SECRET_KEY` environment variable
- Configure production database (MySQL/PostgreSQL)
- Set up proper CORS origins
- Enable HTTPS
- Configure file upload limits
- Set up proper logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow existing code style
- Write clear commit messages
- Test thoroughly before submitting
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

For questions or issues:
- Check the [Issues](../../issues) page
- Review the documentation
- Contact the development team

## 🙏 Acknowledgments

- Built with React, Flask, and modern web technologies
- UI design inspired by modern vacation booking platforms
- Docker containerization for easy deployment

---

**Happy vacation planning! 🏖️**