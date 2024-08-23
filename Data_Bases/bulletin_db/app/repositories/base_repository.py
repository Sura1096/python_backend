from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


class TradingAbstractRepository(ABC):
    @abstractmethod
    async def add_trading_info(self, data: dict):
        raise NotImplementedError


class TradingRepo(TradingAbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_trading_info(self, data: dict):
        stmt = insert(self.model).values(
            exchange_product_id=data['exchange_product_id'],
            exchange_product_name=data['exchange_product_name'],
            oil_id=data['oil_id'],
            delivery_basis_id=data['delivery_basis_id'],
            delivery_basis_name=data['delivery_basis_name'],
            delivery_type_id=data['delivery_type_id'],
            volume=data['volume'],
            total=data['total'],
            count=data['count'],
            date=data['date'],
            created_on=data['created_on'],
            updated_on=data['updated_on'],
        )
        await self.session.execute(stmt)
