from datetime import date, datetime, timedelta

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from src.api.services.trade_service import TradeService
from src.schemas.trade import (
    LastTradeDatesEndpoint,
    TradeDynamicsRequest,
    TradeEndpoint,
    TradeResultsRequest,
)
from src.utils.unit_of_work import UnitOfWork

router = APIRouter(prefix='/trades')


async def get_service(uow: UnitOfWork = Depends(UnitOfWork)) -> TradeService:
    return TradeService(uow)


def cache_time() -> int:
    """Возвращает время жизни (TTL) в секундах до следующего сброса кэша.

    :return: Количество секунд до следующего сброса кэша.
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
) -> LastTradeDatesEndpoint:
    result = {'data': await service.get_last_trading_dates(limit)}
    return LastTradeDatesEndpoint(**result)


@router.get('/dynamics')
@cache(expire=cache_time())
async def get_dynamics(
    start_date: date,
    end_date: date,
    oil_id: str | None = None,
    delivery_basis_id: str | None = None,
    delivery_type_id: str | None = None,
    service: TradeService = Depends(get_service),
) -> TradeEndpoint:
    trade_filters = {
        'start_date': start_date,
        'end_date': end_date,
        'oil_id': oil_id,
        'delivery_basis_id': delivery_basis_id,
        'delivery_type_id': delivery_type_id,
    }
    trade_filters = TradeDynamicsRequest(**trade_filters)
    result = {'data': await service.get_dynamics(trade_filters)}
    return TradeEndpoint(**result)


@router.get('/last_results')
@cache(expire=cache_time())
async def get_trading_results(
    oil_id: str | None = None,
    delivery_basis_id: str | None = None,
    delivery_type_id: str | None = None,
    service: TradeService = Depends(get_service),
) -> TradeEndpoint:
    trade_filters = {
        'oil_id': oil_id,
        'delivery_basis_id': delivery_basis_id,
        'delivery_type_id': delivery_type_id,
    }
    trade_filters = TradeResultsRequest(**trade_filters)
    result = {'data': await service.get_trading_results(trade_filters)}
    return TradeEndpoint(**result)
