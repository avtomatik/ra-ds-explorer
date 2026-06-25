from fastapi import FastAPI

from rads_explorer.infrastructure.fixtures import router

app = FastAPI(title="Registration Authority Data Services Enterprise API")

app.include_router(router, prefix="/api/ra")
