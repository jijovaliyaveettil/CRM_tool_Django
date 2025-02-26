# Django CRM Tool

## Project Overview
A comprehensive Customer Relationship Management (CRM) web application built with Django, designed to help businesses manage their customer interactions, track leads, and streamline sales processes.

## Features
- User Authentication and Authorization
- Lead Management
- Customer Tracking
- Responsive Web Interface
- Dockerized Deployment

## Technologies Used
- Django
- PostgreSQL
- Docker
- Gunicorn
- Nginx

## Prerequisites
- Docker
- Docker Compose
- Git

## Local Development Setup

### Clone the Repository
```bash
git clone https://github.com/jijovaliyaveettil/django-crm-tool.git
cd django-crm-tool
```

### Environment Configuration
1. Create a `.env` file in the project root
2. Add necessary environment variables (database credentials, secret key, etc.)

## Docker Deployment

### Build and Start Containers
```bash
# Build the images
docker-compose build

# Start the containers
docker-compose up

# Start in detached mode
docker-compose up -d
```

### Database Migrations
```bash
# Create migrations
docker-compose exec web python manage.py makemigrations

# Apply migrations
docker-compose exec web python manage.py migrate
```

### Additional Docker Commands
```bash
# Stop containers
docker-compose down

# View logs
docker-compose logs

# Access PostgreSQL shell
docker-compose exec db psql -U postgres

# Collect static files
docker-compose exec web python manage.py collectstatic
```

## Development Workflow
1. Create a virtual environment
2. Install dependencies
3. Set up local PostgreSQL database
4. Run migrations
5. Start the development server

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

