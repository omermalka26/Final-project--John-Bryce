# Database Setup

## Quick Setup

If the database is deleted or corrupted, run:

```bash
python setup_database.py
```

This will:
1. Create all tables (roles, countries, users, vacations, likes)
2. Add User and Admin roles
3. Add 20 countries
4. Create admin user (admin@admin.com / admin)
5. Add 20 sample vacations with future dates
6. Ensure all required images exist

## Admin Credentials

- **Email**: admin@admin.com
- **Password**: admin

## What's Included

- **20 Countries**: Israel, Italy, United States, Canada, Spain, China, France, United Kingdom, India, Japan, Germany, Australia, Brazil, Mexico, South Africa, Egypt, Turkey, Greece, Netherlands, Sweden

- **20 Vacations**: All with future dates (September 2025 - June 2026), proper descriptions, prices in ILS, and images

- **Complete Database**: All tables with proper relationships and constraints
