from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from src.api.routers.trade import router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url('redis://localhost')
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)
