from datetime import datetime, timedelta

from api.services.trade_service import TradeService
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from schemas.trade import (
    LastTradeResponse,
    TradeDynamicsRequest,
    TradeResponse,
    TradeResultsRequest,
)
from utils.unit_of_work import UnitOfWork

router = APIRouter(prefix='/trades')


async def get_service(uow: UnitOfWork = Depends(UnitOfWork)) -> TradeService:
    return TradeService(uow)


def cache_time():
    """Возвращает значение для сброса кэша в 14:11.

    :return: TTL (time-to-live) в секундах.
    """
    now = datetime.now()
    next_reset = now.replace(hour=14, minute=11, second=0, microsecond=0)
    if now >= next_reset:
        next_reset += timedelta(days=1)
    ttl = (next_reset - now).total_seconds()
    return int(ttl)


@router.get('/last_dates')
@cache(expire=cache_time())
async def get_last_trading_dates(
    limit: int,
    service: TradeService = Depends(get_service),
) -> list[LastTradeResponse]:
    return await service.get_last_trading_dates(limit)


@router.get('/dynamics')
@cache(expire=cache_time())
async def get_dynamics(
    trade_filters: TradeDynamicsRequest,
    service: TradeService = Depends(get_service),
) -> list[TradeResponse]:
    return await service.get_dynamics(trade_filters)


@router.get('/last_results')
@cache(expire=cache_time())
async def get_trading_results(
    trade_filters: TradeResultsRequest,
    service: TradeService = Depends(get_service),
) -> list[TradeResponse]:
    return await service.get_trading_results(trade_filters)
