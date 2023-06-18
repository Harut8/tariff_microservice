from fastapi import FastAPI
from api.tariff_api import tariff_router
from uvicorn import run
from repository.core.core import DbConnection

app = FastAPI(version="1.0.0")
app.include_router(tariff_router, prefix="/api/v1")


@app.on_event("startup")
async def on_start_server():
    await DbConnection.create_connection()


@app.get("/")
def ping():
    return {"status": "SERVER RUNNING"}


def run_server():
    run(app, port=8001)
