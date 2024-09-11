from typing import Any

from utils.unit_of_work import UnitOfWork


class TradeService:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def add_new_trade(self, **kwargs: Any) -> None:
        async with self.uow:
            await self.uow.trade.add_trade(**kwargs)
            await self.uow.commit()
