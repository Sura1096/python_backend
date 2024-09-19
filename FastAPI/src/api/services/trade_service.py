from src.schemas.trade import (
    LastTradeRequest,
    LastTradeResponse,
    TradeDynamicsRequest,
    TradeResponse,
    TradeResultsRequest,
)
from src.utils.service import BaseService
from src.utils.unit_of_work import UnitOfWork


class TradeService(BaseService):
    def __init__(self, uow: UnitOfWork) -> None:
        super().__init__(uow)

    async def get_last_trading_dates(
        self,
        filters: LastTradeRequest,
    ) -> list[LastTradeResponse]:
        async with self.uow:
            trades = await self.uow.trade.get_last_trading_dates(filters)
            return [LastTradeResponse(trade_date=trade) for trade in trades]

    async def get_dynamics(
        self,
        trade_filters: TradeDynamicsRequest,
    ) -> list[TradeResponse]:
        async with self.uow:
            trades = await self.uow.trade.get_dynamics(trade_filters)
            return [trade.to_pydantic_schema() for trade in trades]

    async def get_trading_results(
        self,
        trade_filters: TradeResultsRequest,
    ) -> list[TradeResponse]:
        async with self.uow:
            trades = await self.uow.trade.get_trading_results(trade_filters)
            return [trade.to_pydantic_schema() for trade in trades]
