############################
# BASE LAYER
############################
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv==0.5.0

############################
# DEPENDENCIES (LOCKED)
############################
FROM base AS deps

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

############################
# RUNTIME IMAGE (FINAL)
############################
FROM python:3.12-slim AS runtime

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY --from=deps /usr/local /usr/local

COPY gostra ./gostra

EXPOSE 8000

HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "gostra.interfaces.main:app", "--host", "0.0.0.0", "--port", "8000"]
