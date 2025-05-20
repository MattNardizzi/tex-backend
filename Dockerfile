# ───────────────────────────────────────────
# Stage 1: Build all wheels in a throw-away layer
# ───────────────────────────────────────────
FROM python:3.11-slim AS builder

# Install essential build tools and dependencies
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential g++ git curl wget cmake pkg-config \
    libopenblas-dev liblapack-dev libatlas-base-dev \
    libgl1 libglib2.0-0 graphviz libgraphviz-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /wheels

# Copy and build all Python package wheels
COPY requirements.txt .
RUN pip wheel --no-cache-dir -r requirements.txt

# ───────────────────────────────────────────
# Stage 2: Runtime image
# ───────────────────────────────────────────
FROM python:3.11-slim

# Install only runtime dependencies (no compilers)
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    libopenblas0-pthread liblapack3 libatlas3-base \
    libgl1 libglib2.0-0 graphviz \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Bring in pre-built wheels from builder stage
COPY --from=builder /wheels /wheels

# Also need the requirements file again to tell pip what to install
COPY requirements.txt .

# Install dependencies from the wheels (offline, no PyPI)
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt

# Copy the full application source
COPY . .

# Expose the port your Flask app runs on
EXPOSE 8000

# Launch Tex’s Flask API using Gunicorn
CMD ["gunicorn", "-w", "4", "-k", "gthread", "-b", "0.0.0.0:8000", "backend.tex_core_api:app"]
