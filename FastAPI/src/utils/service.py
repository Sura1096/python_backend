from typing import Any

from src.utils.unit_of_work import UnitOfWork


class BaseService:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def add_one(self, **kwargs: Any) -> None:
        async with self.uow:
            await self.uow.trade.add_one(**kwargs)
