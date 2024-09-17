from collections.abc import Sequence

from sqlalchemy import distinct, select

from src.models.spimex_model import SpimexTradingResults
from src.schemas.trade import (
    LastTradeResponse,
    TradeDynamicsRequest,
    TradeResultsRequest,
)
from src.utils.repository import SqlAlchemyRepository


class TradeRepository(SqlAlchemyRepository):
    model = SpimexTradingResults

    async def get_last_trading_dates(self, lim: int) -> Sequence[LastTradeResponse]:
        query = (
            select(distinct(self.model.date))
            .order_by(self.model.date.desc())
            .limit(lim)
        )
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_dynamics(
        self,
        trade_filters: TradeDynamicsRequest,
    ) -> Sequence[SpimexTradingResults]:
        query = select(self.model).filter(
            self.model.date >= trade_filters.start_date,
            self.model.date <= trade_filters.end_date,
        )

        if trade_filters.oil_id:
            query = query.filter(self.model.oil_id == trade_filters.oil_id)
        if trade_filters.delivery_type_id:
            query = query.filter(
                self.model.delivery_type_id == trade_filters.delivery_type_id,
            )
        if trade_filters.delivery_basis_id:
            query = query.filter(
                self.model.delivery_basis_id == trade_filters.delivery_basis_id,
            )
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_trading_results(
        self,
        trade_filters: TradeResultsRequest,
    ) -> Sequence[SpimexTradingResults]:
        query = select(self.model)
        if trade_filters.oil_id:
            query = query.filter(self.model.oil_id == trade_filters.oil_id)
        if trade_filters.delivery_type_id:
            query = query.filter(
                self.model.delivery_type_id == trade_filters.delivery_type_id,
            )
        if trade_filters.delivery_basis_id:
            query = query.filter(
                self.model.delivery_basis_id == trade_filters.delivery_basis_id,
            )
        query = query.order_by(self.model.date.desc())
        result = await self.session.execute(query)
        return result.scalars().all()
