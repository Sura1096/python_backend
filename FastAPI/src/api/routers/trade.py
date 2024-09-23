from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from src.api.services.trade_service import TradeService
from src.schemas.trade import (
    LastTradeDatesEndpoint,
    LastTradeRequest,
    TradeDynamicsRequest,
    TradeEndpoint,
    TradeResultsRequest,
)
from src.schemas.trades_parameters import (
    DynamicsParams,
    LastTradingDatesParams,
    TradingResultsParams,
)
from src.utils.unit_of_work import UnitOfWork

router = APIRouter(prefix='/trades', tags=['trade_info'])


def get_service(uow: UnitOfWork = Depends(UnitOfWork)) -> TradeService:
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
    params: LastTradingDatesParams = Depends(),
    service: TradeService = Depends(get_service),
) -> LastTradeDatesEndpoint:
    filters = LastTradeRequest(limit=params.limit, offset=params.offset)
    result = {'data': await service.get_last_trading_dates(filters)}
    return LastTradeDatesEndpoint(**result)


@router.get('/dynamics')
@cache(expire=cache_time())
async def get_dynamics(
    params: DynamicsParams = Depends(),
    service: TradeService = Depends(get_service),
) -> TradeEndpoint:
    trade_filters = TradeDynamicsRequest(
        start_date=params.start_date,
        end_date=params.end_date,
        limit=params.limit,
        offset=params.offset,
        oil_id=params.oil_id,
        delivery_basis_id=params.delivery_basis_id,
        delivery_type_id=params.delivery_type_id,
    )
    result = {'data': await service.get_dynamics(trade_filters)}
    return TradeEndpoint(**result)


@router.get('/last_results')
@cache(expire=cache_time())
async def get_trading_results(
    params: TradingResultsParams = Depends(),
    service: TradeService = Depends(get_service),
) -> TradeEndpoint:
    trade_filters = TradeResultsRequest(
        limit=params.limit,
        offset=params.offset,
        oil_id=params.oil_id,
        delivery_basis_id=params.delivery_basis_id,
        delivery_type_id=params.delivery_type_id,
    )
    result = {'data': await service.get_trading_results(trade_filters)}
    return TradeEndpoint(**result)
