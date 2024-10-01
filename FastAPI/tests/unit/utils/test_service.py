from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.trade import TradeResponse
from tests.fixtures import FakeBaseService
from tests.utils import compare_dicts_and_db_models


class TestBaseService:
    class _BaseService(FakeBaseService):
        pass

    def __get_service(self, session: AsyncSession) -> FakeBaseService:
        return self._BaseService(session)

    async def test_add_one(
        self,
        transaction_session: AsyncSession,
        trade: dict,
        get_trades,
    ) -> None:
        service = self.__get_service(transaction_session)
        await service.add_one(**trade)

        trades_db = await get_trades()
        assert compare_dicts_and_db_models(trades_db, [trade], TradeResponse)
