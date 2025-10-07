# CodeLeap Backend Test

This is a Django REST Framework API for managing posts.

## Features

- Create, read, update, and delete posts
- No user authentication required
- Posts are stored with username, title, content, and creation timestamp

## API Endpoints

- `POST /api/posts/` - Create a new post
- `GET /api/posts/` - Get all posts (sorted by most recent first)
- `PATCH /api/posts/{id}/` - Update a post
- `DELETE /api/posts/{id}/` - Delete a post

## Running with Docker

1. Build and run the services:
   ```
   docker-compose up --build
   ```

2. Run migrations:
   ```
   docker-compose exec web python src/manage.py migrate
   ```

3. Create a superuser (optional):
   ```
   docker-compose exec web python src/manage.py createsuperuser
   ```

4. Access the API at `http://localhost:8000/`

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