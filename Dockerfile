# ───────────────────────────────────────────
# Stage 1: Build all wheels in a throw-away layer
# ───────────────────────────────────────────
FROM python:3.11-slim AS builder

# OS libs needed for Torch, XGBoost, Graphviz, etc.
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential g++ git curl wget cmake pkg-config \
    libopenblas-dev liblapack-dev libatlas-base-dev \
    libgl1 libglib2.0-0 graphviz libgraphviz-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /wheels

COPY requirements.txt .
RUN pip wheel --no-cache-dir -r requirements.txt

# ───────────────────────────────────────────
# Stage 2: Runtime image
# ───────────────────────────────────────────
FROM python:3.11-slim

# Runtime dependencies (no compilers needed here)
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    libopenblas0-pthread liblapack3 libatlas3-base \
    libgl1 libglib2.0-0 graphviz \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy prebuilt wheels from Stage 1 and install them
COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt

# Copy the entire project
COPY . .

# Gunicorn will serve Flask API on port 8000
EXPOSE 8000
CMD ["gunicorn", "-w", "4", "-k", "gthread", "-b", "0.0.0.0:8000", "backend.tex_core_api:app"]
