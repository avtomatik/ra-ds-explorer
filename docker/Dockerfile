ARG PYTHON_REGISTRY=ffff-fff-fff-ffff-fff-ffffff.ffff.fff.fffffff.fffff/ffff-ffffff
ARG APP_USER=fffffffffffffffffff
ARG APP_UID=0000
ARG APP_GID=0000
ARG HTTPS_PROXY=fffff.fffffff.fffff:0000

FROM ${PYTHON_REGISTRY}/python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd --gid ${APP_GID} ${APP_USER} && \
    useradd --uid ${APP_UID} \
            --gid ${APP_GID} \
            --create-home \
            --shell /bin/bash \
            ${APP_USER}

COPY pyproject.toml uv.lock uv.toml README.md ./

RUN pip install --no-cache-dir --proxy ${HTTPS_PROXY} uv 

RUN uv sync --frozen --no-dev

COPY rads_explorer ./rads_explorer

COPY html ./html

RUN chown -R ${APP_USER}:${APP_USER} /app

USER ${APP_USER}

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/api/ra/health || exit 1

CMD ["/app/.venv/bin/uvicorn", "rads_explorer.interfaces.main:app", "--host", "0.0.0.0", "--port", "8000"]
