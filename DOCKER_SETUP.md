# Docker Setup Guide for A2A Backend

This guide explains how to build and run the A2A Customer Support Agent backend using Docker.

## Prerequisites

- Docker installed and running
- Docker Compose installed
- Google Gemini API key

## Quick Start

### 1. Set up environment variables

Copy the example environment file and add your Google API key:

```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

### 2. Build the Docker image

```bash
docker-compose build
```

### 3. Start the application

```bash
docker-compose up -d
```

The FastAPI backend will be available at `http://localhost:8000`

### 4. Verify the application is running

```bash
# Check health status
curl http://localhost:8000/api/health

# View logs
docker-compose logs -f a2a-backend
```

## API Endpoints

- `GET /` - Web UI interface
- `POST /api/support` - Send a customer support message
- `GET /api/health` - Health check endpoint
- `GET /api/intents` - Get supported intent types
- `GET /docs` - FastAPI Swagger documentation
- `GET /redoc` - FastAPI ReDoc documentation

## Docker Commands

### View logs
```bash
docker-compose logs -f a2a-backend
```

### Stop the application
```bash
docker-compose down
```

### Rebuild the image (after code changes)
```bash
docker-compose build --no-cache
docker-compose up -d
```

### Access the container shell
```bash
docker-compose exec a2a-backend sh
```

### Remove all data and containers
```bash
docker-compose down -v
```

## Environment Variables

The following environment variables are used:

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key | Yes |
| `PYTHONUNBUFFERED` | Disable Python buffering | No (default: 1) |

## Volumes

The following volumes are mounted for development:

- `./A2A` → `/app/A2A` - Backend source code
- `./templates` → `/app/templates` - Jinja2 templates

To disable these for production, remove or modify the `volumes` section in `docker-compose.yml`.

## Health Check

The container includes a built-in health check that pings the `/api/health` endpoint every 30 seconds. You can check the status with:

```bash
docker-compose ps
```

## Production Deployment

For production deployments:

1. Remove the `volumes` section from `docker-compose.yml` to use the image as-is
2. Add environment-specific configuration in the `environment` section
3. Consider using a reverse proxy (nginx) in front of the FastAPI service
4. Update restart policy: `restart: always`
5. Consider resource limits:

```yaml
services:
  a2a-backend:
    # ... other config ...
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
```

## Troubleshooting

### Application won't start
```bash
docker-compose logs a2a-backend
```

### Health check failing
Ensure the GOOGLE_API_KEY environment variable is set correctly.

### Port already in use
Change the port mapping in `docker-compose.yml`:
```yaml
ports:
  - "8001:8000"  # Maps container:8000 to host:8001
```

### API key not recognized
Make sure your `.env` file is in the root directory and contains the correct `GOOGLE_API_KEY`.

## Building without Docker Compose

To build and run without Docker Compose:

```bash
# Build the image
docker build -t a2a-customer-support:latest .

# Run the container
docker run -d \
  --name a2a-backend \
  -p 8000:8000 \
  -e GOOGLE_API_KEY=your_api_key \
  -v $(pwd)/A2A:/app/A2A \
  -v $(pwd)/templates:/app/templates \
  a2a-customer-support:latest

# View logs
docker logs -f a2a-backend
```

## Next Steps

- Access the web UI at http://localhost:8000
- Try the Swagger API docs at http://localhost:8000/docs
- Test with: `curl -X POST http://localhost:8000/api/support -H "Content-Type: application/json" -d '{"message": "Where is my order?"}'`
