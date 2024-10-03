from src.schemas.trade import TradeResponse
from src.utils.service import BaseService
from src.utils.unit_of_work import UnitOfWork
from tests.utils import compare_dicts_and_db_models


class TestBaseService:
    class _BaseService(BaseService):
        pass

    def __get_service(self) -> BaseService:
        return self._BaseService(UnitOfWork())

    async def test_add_one(
        self,
        trade: dict,
        get_trades,
    ) -> None:
        service = self.__get_service()
        await service.add_one(**trade)

        trades_db = await get_trades()
        assert compare_dicts_and_db_models(trades_db, [trade], TradeResponse)
