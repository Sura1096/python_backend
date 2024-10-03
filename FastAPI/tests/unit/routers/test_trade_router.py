from typing import Any

import pytest
from httpx import AsyncClient
from tests import fixtures


@pytest.mark.usefixtures('setup_trade_info')
class TestTradeRouter:
    @staticmethod
    @pytest.mark.parametrize(
        ('url', 'expected_status_code', 'params', 'expected_result', 'expectation'),
        fixtures.test_cases.PARAMS_TEST_LAST_TRADING_DATES,
    )
    async def test_get_last_trading_dates(
        url: str,
        expected_status_code: int,
        params: dict,
        expected_result: dict,
        expectation: Any,
        async_client: AsyncClient,
    ) -> None:
        with expectation:
            response = await async_client.get(url, params=params)

            assert response.status_code == expected_status_code
            assert response.json() == expected_result

    @staticmethod
    @pytest.mark.parametrize(
        ('url', 'expected_status_code', 'params', 'expected_result', 'expectation'),
        fixtures.test_cases.PARAMS_TEST_GET_DYNAMICS,
    )
    async def test_get_dynamics(
        url: str,
        expected_status_code: int,
        params: dict,
        expected_result: dict,
        expectation: Any,
        async_client: AsyncClient,
    ) -> None:
        with expectation:
            response = await async_client.get(url, params=params)

            assert response.status_code == expected_status_code
            assert response.json() == expected_result

    @staticmethod
    @pytest.mark.parametrize(
        ('url', 'expected_status_code', 'params', 'expected_result', 'expectation'),
        fixtures.test_cases.PARAMS_TEST_TRADING_RESULTS,
    )
    async def test_get_trading_results(
        url: str,
        expected_status_code: int,
        params: dict,
        expected_result: dict,
        expectation: Any,
        async_client: AsyncClient,
    ) -> None:
        with expectation:
            response = await async_client.get(url, params=params)

            assert response.status_code == expected_status_code
            assert response.json() == expected_result
