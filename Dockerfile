# ───────────────────────────────────────────
# Stage 1: build all wheels in a throw-away layer
# ───────────────────────────────────────────
FROM python:3.11-slim AS builder

# OS libs needed by Torch / XGBoost / CatBoost / LightGBM / Graphviz / etc.
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential g++ git curl wget cmake pkg-config \
        libopenblas-dev liblapack-dev libatlas-base-dev \
        libgl1 libglib2.0-0 graphviz libgraphviz-dev \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /wheels

COPY requirements.txt .
RUN pip wheel --no-cache-dir -r requirements.txt

# ───────────────────────────────────────────
# Stage 2: runtime image
# ───────────────────────────────────────────
FROM python:3.11-slim

# Same system libs required at runtime (no compilers)
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        libopenblas0-pthread liblapack3 libatlas3-base \
        libgl1 libglib2.0-0 graphviz \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install pre-built wheels from builder
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir -r /wheels/requirements.txt

# Copy your project
COPY . .

# Gunicorn will serve Flask on port 8000
EXPOSE 8000
CMD ["gunicorn", "-w", "4", "-k", "gthread", "-b", "0.0.0.0:8000", "backend.tex_core_api:app"]