import asyncio
from collections.abc import AsyncGenerator, Generator

import pytest
import pytest_asyncio
import sqlalchemy.schema
from httpx import AsyncClient
from sqlalchemy import Result, sql
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from src.api.services.trade_service import TradeService
from src.core.config import test_db
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
    engine = create_async_engine(
        test_db.test_db_url(),
        echo=False,
        future=True,
    ).execution_options(compiled_cache=None)

    yield engine

    await engine.dispose()


@pytest_asyncio.fixture(scope='session', autouse=True)
async def setup_schemas(db_engine: AsyncEngine) -> None:
    schemas = ('schema_for_example',)
    async with db_engine.connect() as conn:
        for schema in schemas:
            try:
                await conn.execute(sqlalchemy.schema.CreateSchema(schema))
            except Exception as e:
                if 'already exists' in str(e):
                    pass
                else:
                    raise
            await conn.commit()


@pytest_asyncio.fixture(scope='session', autouse=True)
async def setup_db(db_engine: AsyncEngine, setup_schemas: None) -> None:
    async with db_engine.begin() as db_conn:
        await db_conn.run_sync(Base.metadata.drop_all)
        await db_conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture
async def transaction_session(
    db_engine: AsyncEngine,
) -> AsyncGenerator[AsyncSession, None]:
    connection = await db_engine.connect()
    await connection.begin()
    session = AsyncSession(bind=connection)

    yield session

    await session.rollback()
    await connection.close()


@pytest_asyncio.fixture
def fake_trade_service(
    transaction_session: AsyncSession,
) -> Generator[FakeTradeService, None]:
    _fake_trade_service = FakeTradeService(transaction_session)
    yield _fake_trade_service


@pytest_asyncio.fixture
async def async_client(
    fake_trade_service: FakeTradeService,
) -> AsyncGenerator[AsyncClient, None]:
    app.dependency_overrides[TradeService] = lambda: fake_trade_service
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac
