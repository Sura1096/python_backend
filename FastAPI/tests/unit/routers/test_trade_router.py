from datetime import date

import pytest
from httpx import AsyncClient
from src.schemas.trade import TradeResponse
from tests.utils import (
    check_response_get_dynamics,
    check_response_get_last_trading_dates,
)


@pytest.mark.usefixtures('setup_trade_info')
class TestLastTradingDates:
    @staticmethod
    async def test_get_last_trading_dates(
        async_client: AsyncClient,
        trade: dict,
    ) -> None:
        params = {
            'limit': 1,
            'offset': 0,
        }
        response = await async_client.get('/trades/last_dates', params=params)

        assert response.status_code == 200
        assert len(response.json()['data']) == 1
        assert check_response_get_last_trading_dates(response.json()['data'], [trade])

    @staticmethod
    async def test_get_last_trading_dates_empty_answer(
        async_client: AsyncClient,
    ) -> None:
        params = {
            'limit': 1,
            'offset': 2,
        }
        response = await async_client.get('/trades/last_dates', params=params)

        assert response.status_code == 200
        assert len(response.json()['data']) == 0


@pytest.mark.usefixtures('setup_trade_info')
class TestGetDynamics:
    @staticmethod
    async def test_get_dynamics_with_required_params(
        async_client: AsyncClient,
        trade: dict,
    ) -> None:
        params = {
            'start_date': date.fromisoformat('2023-12-26'),
            'end_date': date.fromisoformat('2023-12-27'),
            'limit': 1,
            'offset': 0,
        }
        response = await async_client.get('/trades/dynamics', params=params)

        assert response.status_code == 200
        assert len(response.json()['data']) == 1
        assert check_response_get_dynamics(
            response.json()['data'],
            [trade],
            TradeResponse,
        )

    @staticmethod
    async def test_get_dynamics_with_all_params(
        async_client: AsyncClient,
        trade: dict,
    ) -> None:
        params = {
            'start_date': date.fromisoformat('2023-12-26'),
            'end_date': date.fromisoformat('2023-12-27'),
            'limit': 1,
            'offset': 0,
            'oil_id': 'A100',
            'delivery_basis_id': 'ANK',
            'delivery_type_id': 'F',
        }
        response = await async_client.get('/trades/dynamics', params=params)

        assert response.status_code == 200
        assert len(response.json()['data']) == 1
        assert check_response_get_dynamics(
            response.json()['data'],
            [trade],
            TradeResponse,
        )

    @staticmethod
    async def test_get_dynamics_empty_answer(
        async_client: AsyncClient,
    ) -> None:
        params = {
            'start_date': date.fromisoformat('2023-12-28'),
            'end_date': date.fromisoformat('2023-12-29'),
            'limit': 1,
            'offset': 0,
            'oil_id': 'A100',
            'delivery_basis_id': 'ANK',
            'delivery_type_id': 'F',
        }
        response = await async_client.get('/trades/dynamics', params=params)

        assert response.status_code == 200
        assert len(response.json()['data']) == 0


@pytest.mark.usefixtures('setup_trade_info')
class TestTradingResults:
    @staticmethod
    async def test_get_trading_results_with_all_params(
        async_client: AsyncClient,
        trade: dict,
    ) -> None:
        params = {
            'limit': 1,
            'offset': 0,
            'oil_id': 'A100',
            'delivery_basis_id': 'ANK',
            'delivery_type_id': 'F',
        }
        response = await async_client.get('/trades/last_results', params=params)

        assert response.status_code == 200
        assert len(response.json()['data']) == 1
        assert check_response_get_dynamics(
            response.json()['data'],
            [trade],
            TradeResponse,
        )

    @staticmethod
    async def test_get_trading_results_with_required_params(
        async_client: AsyncClient,
        trade: dict,
    ) -> None:
        params = {
            'limit': 1,
            'offset': 0,
        }
        response = await async_client.get('/trades/last_results', params=params)

        assert response.status_code == 200
        assert len(response.json()['data']) == 1
        assert check_response_get_dynamics(
            response.json()['data'],
            [trade],
            TradeResponse,
        )

    @staticmethod
    async def test_get_trading_results_empty_answer(
        async_client: AsyncClient,
    ) -> None:
        params = {
            'limit': 1,
            'offset': 0,
            'oil_id': 'A299',
            'delivery_basis_id': 'ANK',
            'delivery_type_id': 'F',
        }
        response = await async_client.get('/trades/last_results', params=params)

        assert response.status_code == 200
        assert len(response.json()['data']) == 0
