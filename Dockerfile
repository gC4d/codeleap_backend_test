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
 && update-ca-certificates

RUN addgroup -S appuser && adduser -S -G appuser appuser

COPY --from=builder /install /usr/local

WORKDIR /app
COPY . .
RUN chown -R appuser:appuser /app

USER appuser

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 8000
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
