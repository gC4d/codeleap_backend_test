# CodeLeap Backend Test

This is a Django REST Framework API for managing posts with Docker support.

## Features

- Create, read, update, and delete posts
- No user authentication required
- Posts are stored with username, title, content, and creation timestamp
- Automatic database migration on container startup
- Dockerized for easy deployment

## API Endpoints

- `POST /api/posts/` - Create a new post (requires username, title, content)
- `GET /api/posts/` - Get all posts (sorted by most recent first)
- `PATCH /api/posts/{id}/` - Update a post (only title and content can be modified)
- `DELETE /api/posts/{id}/` - Delete a post

## Running with Docker

The application includes an entrypoint script that automatically waits for the database to be ready and runs migrations.

1. Build and run the services:
   ```
   docker-compose up --build
   ```

2. Access the API at `http://localhost:8000/`

3. Create a superuser (optional):
   ```
   docker-compose exec web python src/manage.py createsuperuser
   ```

## Running without Docker

1. Install dependencies:
   ```
   pip install -e .
   ```

2. Set up the database:
   ```
   python src/manage.py migrate
   ```

3. Create a superuser (optional):
   ```
   python src/manage.py createsuperuser
   ```

4. Run the development server:
   ```
   python src/manage.py runserver
   ```

5. Access the API at `http://localhost:8000/`

## Development

- The application uses Django REST Framework with ModelViewSet
- PostgreSQL database with automatic migration handling
- Alpine-based Docker images for security and smaller size
- Non-root user execution for container security