# syntax=docker/dockerfile:1.4
# Build stage
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install uv as a faster alternative to pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uv && \
    rm -rf /root/.cache/pip/*

# Copy dependency files first for better layer caching
COPY pyproject.toml requirements.txt ./

# Install dependencies using uv for better performance
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install -r requirements.txt

# Copy application code
COPY . .

# Runtime stage
FROM python:3.12-slim AS runtime

WORKDIR /app

# Install only the necessary runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for running the application
RUN useradd -m appuser

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY --from=builder /build /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_ENV=production \
    PORT=8000

# Switch to non-root user
USER appuser

# Create directory for any app-generated files with proper permissions
RUN mkdir -p /app/data /app/logs
VOLUME ["/app/data", "/app/logs"]

# Expose the API port
EXPOSE ${PORT}

# Health check to enable orchestration
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

# Start the application with proper signal handling
CMD ["sh", "-c", "exec python app.py"] 