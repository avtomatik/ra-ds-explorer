from fastapi import FastAPI

from rads_explorer.interfaces.api.routes import router

app = FastAPI(title="Registration Authority Data Services Enterprise API")

app.include_router(router, prefix="/api/ra")
