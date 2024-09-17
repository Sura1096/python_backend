from fastapi import APIRouter, Depends

from src.api.services.trade_service import TradeService
from src.schemas.trade import (
    LastTradeResponse,
    TradeDynamicsRequest,
    TradeResponse,
    TradeResultsRequest,
)
from src.utils.unit_of_work import UnitOfWork

router = APIRouter(prefix='/trades')


async def get_service(uow: UnitOfWork = Depends(UnitOfWork)) -> TradeService:
    return TradeService(uow)


@router.get('/last_dates')
async def get_last_trading_dates(
    limit: int,
    service: TradeService = Depends(get_service),
) -> list[LastTradeResponse]:
    return await service.get_last_trading_dates(limit)


@router.get('/dynamics')
async def get_dynamics(
    trade_filters: TradeDynamicsRequest,
    service: TradeService = Depends(get_service),
) -> list[TradeResponse]:
    return await service.get_dynamics(trade_filters)


@router.get('/last_results')
async def get_trading_results(
    trade_filters: TradeResultsRequest,
    service: TradeService = Depends(get_service),
) -> list[TradeResponse]:
    return await service.get_trading_results(trade_filters)
