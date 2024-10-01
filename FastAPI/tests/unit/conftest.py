from collections.abc import Sequence
from copy import deepcopy
from typing import Any

import pytest
import pytest_asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.spimex_model import SpimexTradingResults

from tests import fixtures
from tests.utils import save_object


@pytest_asyncio.fixture
async def setup_trade_info(
    transaction_session: AsyncSession,
    trade: dict[str, Any],
) -> None:
    await save_object(transaction_session, SpimexTradingResults, trade)


@pytest_asyncio.fixture
async def get_trades(transaction_session: AsyncSession):
    async def _get_trades() -> Sequence[SpimexTradingResults]:
        res = await transaction_session.execute(select(SpimexTradingResults))
        return res.scalars().all()

    return _get_trades


@pytest.fixture
def trade() -> dict[str, Any]:
    return deepcopy(fixtures.postgres.TRADES)
