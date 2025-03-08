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