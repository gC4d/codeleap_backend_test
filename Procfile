release: python src/manage.py migrate
web: gunicorn src.config.asgi:application --bind 0.0.0.0:8000
