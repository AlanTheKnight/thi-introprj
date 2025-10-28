# Multi-stage build for optimized production image
FROM python:3.11-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies needed for building
RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    gcc \
    g++ \
    build-essential \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Configure Poetry: Don't create virtual environment (we're in container)
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VENV_IN_PROJECT=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Copy Poetry files
COPY bot/pyproject.toml bot/poetry.lock ./

# Install dependencies globally
RUN poetry config virtualenvs.create false && \
    poetry install --only=main --no-root && \
    rm -rf $POETRY_CACHE_DIR

# Production stage
FROM python:3.11-slim AS production

ENV DEBIAN_FRONTEND=noninteractive

# Install runtime dependencies only
RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user and set up directories
RUN groupadd -r appuser && useradd -r -g appuser appuser && \
    mkdir -p /app/tmp && \
    chown -R appuser:appuser /app && \
    chmod 755 /tmp && \
    chmod 1777 /tmp

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy application code
COPY --chown=appuser:appuser bot/ .

# Copy training data
COPY --chown=appuser:appuser training/ /app/training/

# Download spaCy model (before switching to non-root user)
RUN python -m spacy download en_core_web_sm

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run gunicorn with configuration file
CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]