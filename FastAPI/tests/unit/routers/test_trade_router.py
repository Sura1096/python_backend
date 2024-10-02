from datetime import date

import pytest
from httpx import AsyncClient
from src.schemas.trade import TradeResponse
from tests.utils import (
    check_response_get_dynamics,
    check_response_get_last_trading_dates,
)


class TestTradeRouter:
    @staticmethod
    @pytest.mark.usefixtures('setup_trade_info')
    async def test_get_last_trading_dates(
        async_client: AsyncClient,
    ) -> None:
        params = {
            'limit': 1,
            'offset': 0,
        }
        response = await async_client.get('/trades/last_dates', params=params)
        print(response.json())

        assert response.status_code == 200
        # assert len(response.json()['data']) == 1
        # assert response.json()['data'][0]['trade_date'] == '2023-12-26'
