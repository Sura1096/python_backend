import asyncio
from collections.abc import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from httpx import AsyncClient
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from src.api.services.trade_service import TradeService
from src.core.config import settings
from src.main import app
from src.models.base import Base
from src.models.spimex_model import SpimexTradingResults

from tests.fixtures import FakeTradeService


@pytest.fixture(scope='session')
def event_loop(request: pytest.FixtureRequest) -> asyncio.AbstractEventLoop:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='session')
async def db_engine() -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(settings.DB_URL)
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture(scope='session', autouse=True)
async def setup_db(db_engine: AsyncEngine) -> None:
    assert settings.MODE == 'TEST'
    async with db_engine.begin() as db_conn:
        await db_conn.run_sync(Base.metadata.drop_all)
        await db_conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture
async def transaction_session(
    db_engine: AsyncEngine,
) -> AsyncGenerator[AsyncSession, None]:
    print('1')
    connection = await db_engine.connect()
    await connection.begin()
    session = AsyncSession(bind=connection)

    yield session

    await connection.commit()  # Сохраняет данные в тестовую БД
    await connection.close()


@pytest_asyncio.fixture
def fake_trade_service(
    transaction_session: AsyncSession,
) -> Generator[FakeTradeService, None]:
    fake_trade_service = FakeTradeService(transaction_session)
    yield fake_trade_service


@pytest_asyncio.fixture
async def async_client(
    fake_trade_service: FakeTradeService,
) -> AsyncGenerator[AsyncClient, None]:
    app.dependency_overrides[TradeService] = lambda: fake_trade_service
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac


@pytest.fixture(scope='session', autouse=True)
def init_cache() -> None:
    redis = aioredis.from_url('redis://localhost')
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
