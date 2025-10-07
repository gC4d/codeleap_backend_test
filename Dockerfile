FROM python:3.13-alpine AS builder

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    python3-dev

WORKDIR /app
COPY pyproject.toml uv.lock ./

RUN pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir --prefix=/install -e .

FROM python:3.13-alpine

RUN apk add --no-cache \
    libpq \
    libffi \
    ca-certificates \
    bash \
    netcat-openbsd \
 && update-ca-certificates

RUN addgroup -S appuser && adduser -S -G appuser appuser

COPY --from=builder /install /usr/local

WORKDIR /app
COPY .env .
COPY . .
RUN chown -R appuser:appuser /app

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown appuser:appuser /entrypoint.sh

USER appuser

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    DJANGO_SETTINGS_MODULE=config.settings

EXPOSE 8000

# Heroku will override the port with $PORT environment variable
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:$PORT", "--timeout", "120", "--keep-alive", "5", "--max-requests", "100", "--max-requests-jitter", "10", "--log-level", "debug", "--access-logfile", "-", "--error-logfile", "-"]
