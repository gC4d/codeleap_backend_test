#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Wait for the database to be ready
echo "Waiting for database..."
while ! nc -z $DB_HOST $DB_PORT; do
    echo "Waiting for PostgreSQL to start on $DB_HOST:$DB_PORT..."
    sleep 1
done

echo "Database is ready!"

# Run migrations
echo "Running migrations..."
python src/manage.py migrate --noinput

# Collect static files (if needed)
# echo "Collecting static files..."
# python src/manage.py collectstatic --noinput

# Create superuser (if needed)
# echo "Creating superuser..."
# python src/manage.py createsuperuser --noinput

# Start the application
exec "$@"
