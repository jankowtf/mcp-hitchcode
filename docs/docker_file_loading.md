# Docker File Loading

This document explains how to use the Docker file loading functionality in templates.

## Overview

The Docker file loading functionality allows you to include content from Dockerfile and docker-compose.yml files in your templates. This is useful for creating templates that include Docker configurations without duplicating the content.

## Directory Structure

Docker files are stored in the `templates/docker` directory. The directory structure is as follows:

```
templates/
  docker/
    python/
      Dockerfile
    multi-container/
      docker-compose.yml
    ...
```

## Usage in Templates

To include a Dockerfile in your template, use the `docker_file` function:

```jinja
{{ docker_file('python/Dockerfile') }}
```

To include a docker-compose.yml file in your template, use the `docker_compose` function:

```jinja
{{ docker_compose('multi-container/docker-compose.yml') }}
```

The path is relative to the `templates/docker` directory.

## Docker Best Practices

Our Docker files follow these best practices:

1. **Multi-stage builds**: We use multi-stage builds to keep the final image size small and avoid including build dependencies in the runtime image.

2. **Using uv for Python package management**: We use [uv](https://github.com/astral-sh/uv) for faster, more reliable Python package management.

3. **Running as non-root user**: We create and use a non-root user for better security.

4. **Environment variables**: We set appropriate environment variables like `PYTHONUNBUFFERED=1`.

5. **Minimal base images**: We use slim variants of official images to reduce image size.

6. **Proper layer caching**: We organize COPY commands to maximize layer caching.

Example of a best-practice Dockerfile:

```dockerfile
# Build stage
FROM python:3.11-slim AS builder

WORKDIR /build

# Install uv for faster, more reliable package management
RUN pip install --no-cache-dir uv

# Copy dependency files
COPY pyproject.toml .
COPY requirements.txt .

# Create and activate virtual environment, install dependencies
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN uv pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copy virtual environment from builder stage
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy application code
COPY . .

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Run as non-root user for better security
RUN useradd -m appuser
USER appuser

# Expose application port
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
```

## Example Template

Here's an example template that includes both a Dockerfile and a docker-compose.yml file:

```jinja
---
version: 1.0.0
created: 2025-03-08
description: Example template demonstrating Docker file loading
variables:
  - docker_file_path: Path to the Dockerfile to include
  - docker_compose_path: Path to the docker-compose.yml file to include
---

# Docker Configuration Example

## Dockerfile

```dockerfile
{{ docker_file(docker_file_path) }}
```

## Docker Compose

```yaml
{{ docker_compose(docker_compose_path) }}
```
```

## API Reference

### `docker_file(file_path: str) -> str`

Load a Dockerfile from the templates directory.

- `file_path`: The path to the Dockerfile, relative to the Docker files directory.
- Returns: The Dockerfile content.
- Raises: `FileNotFoundError` if the Dockerfile does not exist.

### `docker_compose(file_path: str) -> str`

Load a docker-compose.yml file from the templates directory.

- `file_path`: The path to the docker-compose.yml file, relative to the Docker files directory.
- Returns: The docker-compose.yml content.
- Raises: `FileNotFoundError` if the docker-compose.yml file does not exist.

### `load_docker_file(file_path: str) -> str`

Load any Docker file from the templates directory.

- `file_path`: The path to the Docker file, relative to the Docker files directory.
- Returns: The Docker file content.
- Raises: `FileNotFoundError` if the Docker file does not exist.

### `clear_docker_file_cache() -> None`

Clear the Docker file cache.

## Error Handling

If a Docker file is not found, a `FileNotFoundError` will be raised with a message indicating the file path that was not found. You can handle this error in your code to provide a more user-friendly error message. 