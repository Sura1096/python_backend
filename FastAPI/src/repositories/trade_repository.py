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
        """Возвращает список дат последних торговых дней.

        :param lim: Количество последних торговых дат, которые нужно вернуть.
        :return: Список объектов, представляющих последние торговые даты.
        """
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
        """Возвращает список торгов за заданный период.

        :param trade_filters: Объект с фильтрами для запроса данных:
            - start_date (Начальная дата). Обязательный параметр, чтобы определить, от какой даты начинать выборку;
            - end_date (Конечная дата). Обязательный параметр для установки границы выборки;
            - oil_id. Необязательный параметр;
            - delivery_type_id. Необязательный параметр;
            - delivery_basis_id. Необязательный параметр.

        :return: Список объектов, представляющих результаты торговли в заданном диапазоне.
        """
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
        """Возвращает список последних торгов.

        :param trade_filters: Объект с фильтрами для запроса данных:
            - oil_id. Необязательный параметр;
            - delivery_type_id. Необязательный параметр;
            - delivery_basis_id. Необязательный параметр.

        :return: Список объектов, представляющих результаты торговли, удовлетворяющие фильтрам.
        """
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
