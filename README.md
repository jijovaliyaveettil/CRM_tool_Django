# Build the images
docker-compose build

# Start the containers
docker-compose up

# To run in detached mode
docker-compose up -d

# Stop containers
docker-compose down

# View logs
docker-compose logs

# Access PostgreSQL shell
docker-compose exec db psql -U postgres

# Make migrations
docker-compose exec web python manage.py makemigrations

# Collect static files
docker-compose exec web python manage.py collectstatic