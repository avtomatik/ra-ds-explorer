FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock README.md ./

RUN uv sync --frozen --no-dev

COPY rads_explorer ./rads_explorer

EXPOSE 8000

HEALTHCHECK CMD curl --silent --fail http://localhost:8000/health || exit 1

CMD ["/app/.venv/bin/uvicorn", "rads_explorer.interfaces.main:app", "--host", "0.0.0.0", "--port", "8000"]
