# Stage 1: Builder stage
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv with pip and clean cache
RUN pip install --no-cache-dir uv && \
    rm -rf /root/.cache/pip/*

# Copy project files needed for building
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Build the package using uv
RUN uv pip install --system build && \
    python -m build --wheel . && \
    rm -rf /root/.cache/pip/* /root/.cache/uv/*

# Stage 2: Runtime stage
FROM python:3.12-slim AS runtime

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy and install only the built wheel from the builder stage
COPY --from=builder /build/dist/*.whl ./
RUN pip install --no-cache-dir ./*.whl fastapi uvicorn && \
    rm -f ./*.whl

# Create examples directory
RUN mkdir -p /app/examples

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_ENV=development \
    PORT=8001

# Expose the API port
EXPOSE ${PORT}

# Default command - using the example API directly
CMD ["sh", "-c", "uvicorn examples.api.main:app --host 0.0.0.0 --port ${PORT} --reload"] 