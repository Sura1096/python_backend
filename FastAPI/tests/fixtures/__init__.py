__all__ = [
    'FakeBaseService',
    'FakeTradeService',
    'FakeUnitOfWork',
    'postgres',
]


from types import TracebackType

from sqlalchemy.ext.asyncio import AsyncSession
from src.api.services.trade_service import TradeService
from src.repositories.trade_repository import TradeRepository
from src.utils.service import BaseService
from src.utils.unit_of_work import UnitOfWork

from tests.fixtures import postgres


class FakeUnitOfWork(UnitOfWork):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__()
        self._session = session

    async def __aenter__(self) -> None:
        self.trade = TradeRepository(self._session)

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self._session.flush()


class FakeBaseService(BaseService):
    def __init__(self, session: AsyncSession) -> None:
        self.uow = FakeUnitOfWork(session)
        super().__init__(self.uow)


class FakeTradeService(FakeBaseService, TradeService):
    pass
