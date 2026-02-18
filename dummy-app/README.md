# Dummy Express App

A minimal Express.js application for demonstrating Docker multi-stage builds.

## Features

- Basic Express server
- Simple REST endpoints
- Health check endpoint
- Environment variable support

## Endpoints

- `GET /` - Welcome message with timestamp
- `GET /health` - Health check endpoint
- `GET /api/info` - Application information

## Local Development

```bash
# Install dependencies
npm install

# Run the app
npm start
```

The app will run on `http://localhost:3000`

## Docker

This app uses a multi-stage Dockerfile for optimized builds.

### Build the Docker image

```bash
docker build -t dummy-express-app .
```

### Run the container

```bash
docker run -p 3000:3000 dummy-express-app
```

### Using Docker Compose

```bash
# Start the app
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the app
docker-compose down
```

### Multi-Stage Build Explanation

The Dockerfile uses two stages:

1. **Builder Stage**: Uses `node:18-alpine` to install all dependencies
2. **Production Stage**: Creates a lean image with only production dependencies and app code

Benefits:
- Smaller final image size
- Better security (non-root user)
- Optimized layer caching
- Includes health check
