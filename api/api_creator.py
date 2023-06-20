from fastapi import FastAPI
from api.tariff_api import tariff_router
from uvicorn import run
from repository.core.core import DbConnection
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache import FastAPICache
import aioredis


app = FastAPI(version="1.0.0")
app.include_router(tariff_router, prefix="/api/v1")


@app.on_event("startup")
async def on_start_server():
    await DbConnection.create_connection()
    _redis = aioredis.from_url('redis://localhost:6379/2')
    print(_redis)
    FastAPICache.init(RedisBackend(_redis))


@app.get("/")
def ping():
    return {"status": "SERVER RUNNING"}


def run_server():
    run(app, port=8001)
