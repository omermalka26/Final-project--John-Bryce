# Vacation Project - Docker Setup

This project has been configured to run with Docker and MySQL database.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. **Clone the repository** (if not already done)

2. **Run the entire stack with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

   This will:
   - Build and start the MySQL database
   - Build and start the Flask backend
   - Build and start the React frontend
   - Automatically create database tables and populate with initial data

3. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5001
   - MySQL Database: localhost:3306

## Services

### MySQL Database
- **Container**: `vacation_mysql`
- **Port**: 3306
- **Database**: `vacationdb`
- **Username**: `vacationuser`
- **Password**: `vacationpass`
- **Root Password**: `rootpassword`

### Backend (Flask)
- **Container**: `vacation_backend`
- **Port**: 5001
- **Environment**: Production
- **Auto-creates tables and populates initial data**

### Frontend (React)
- **Container**: `vacation_frontend`
- **Port**: 3000
- **Development server with hot reload**

## Useful Commands

### Start services in background:
```bash
docker-compose up -d --build
```

### View logs:
```bash
docker-compose logs -f
```

### Stop all services:
```bash
docker-compose down
```

### Stop and remove volumes (WARNING: This will delete all data):
```bash
docker-compose down -v
```

### Rebuild specific service:
```bash
docker-compose up --build backend
```

### Access MySQL database directly:
```bash
docker exec -it vacation_mysql mysql -u vacationuser -p vacationdb
```

### Access backend container:
```bash
docker exec -it vacation_backend bash
```

### Access frontend container:
```bash
docker exec -it vacation_frontend sh
```

## Database Management

The database is automatically initialized with:
- User and Admin roles
- 20 countries
- Admin user (admin@admin.com / admin)
- 20 sample vacations

## Environment Variables

The following environment variables are configured in docker-compose.yml:

### MySQL:
- `MYSQL_ROOT_PASSWORD`: rootpassword
- `MYSQL_DATABASE`: vacationdb
- `MYSQL_USER`: vacationuser
- `MYSQL_PASSWORD`: vacationpass

### Backend:
- `MYSQL_HOST`: mysql
- `MYSQL_PORT`: 3306
- `MYSQL_DATABASE`: vacationdb
- `MYSQL_USER`: vacationuser
- `MYSQL_PASSWORD`: vacationpass
- `JWT_SECRET_KEY`: your-super-secret-jwt-key-change-in-production

## Troubleshooting

### If containers fail to start:
1. Check if ports 3000, 5001, and 3306 are available
2. Run `docker-compose down` and try again
3. Check logs with `docker-compose logs`

### If database connection fails:
1. Ensure MySQL container is running: `docker-compose ps`
2. Check MySQL logs: `docker-compose logs mysql`
3. Wait a few seconds for MySQL to fully initialize

### If you need to reset the database:
```bash
docker-compose down -v
docker-compose up --build
```

## Development

For development, you can run individual services:

### Backend only:
```bash
cd vite-backend
docker build -t vacation-backend .
docker run -p 5001:5001 --env-file .env vacation-backend
```

### Frontend only:
```bash
cd client
docker build -t vacation-frontend .
docker run -p 3000:3000 vacation-frontend
```

## Production Deployment

For production deployment, consider:
1. Changing default passwords
2. Using environment-specific configuration
3. Setting up proper SSL certificates
4. Using a reverse proxy (nginx)
5. Setting up proper logging and monitoring






