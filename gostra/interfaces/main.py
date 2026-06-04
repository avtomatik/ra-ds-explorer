from fastapi import FastAPI

from gostra.interfaces.api.routes import router

app = FastAPI(title="Gostra Enterprise API")

app.include_router(router, prefix="/api/ra")
