#!/bin/bash
set -e

export PYTHONPATH=/app/src:$PYTHONPATH

export DJANGO_SETTINGS_MODULE=config.settings

if [ -f .env ]; then
    export $(cat .env | xargs)
fi

echo "Waiting for database..."
while ! nc -z $DB_HOST $DB_PORT; do
    echo "Waiting for PostgreSQL to start on $DB_HOST:$DB_PORT..."
    sleep 1
done

echo "Database is ready!"

echo "Running migrations..."
python src/manage.py migrate --noinput

echo "Checking memory usage..."
free -h

echo "Starting application with detailed logging..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --timeout 120 --keep-alive 5 --max-requests 100 --max-requests-jitter 10 --log-level debug --access-logfile - --error-logfile -
