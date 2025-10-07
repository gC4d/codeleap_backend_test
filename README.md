# CodeLeap Backend Test

This is a Django REST Framework API for managing posts with Docker support, including likes and comments.

## Features

- Create, read, update, and delete posts
- Like posts (one like per user per post)
- Add comments to posts
- No user authentication required
- Posts are stored with username, title, content, and creation timestamp
- Automatic database migration on container startup
- Dockerized for easy deployment
- Code follows DRY principles with abstract base models

## API Endpoints

### Posts
- `POST /api/posts/` - Create a new post (requires username, title, content)
- `GET /api/posts/` - Get all posts (sorted by most recent first, includes likes_count and comments_count)
- `GET /api/posts/{id}/` - Get a specific post
- `PATCH /api/posts/{id}/` - Update a post (only title and content can be modified)
- `DELETE /api/posts/{id}/` - Delete a post

### Likes
- `POST /api/likes/` - Like a post (requires post ID and username)
- `GET /api/likes/` - Get all likes (optionally filter by post with ?post={id})
- `DELETE /api/likes/{id}/` - Unlike a post

### Comments
- `POST /api/comments/` - Add a comment to a post (requires post ID, username, and content)
- `GET /api/comments/` - Get all comments (optionally filter by post with ?post={id})
- `PATCH /api/comments/{id}/` - Update a comment (only content can be modified)
- `DELETE /api/comments/{id}/` - Delete a comment

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
- Abstract base models for code reuse (TimestampedModel)
- Automatic counting of likes and comments on posts