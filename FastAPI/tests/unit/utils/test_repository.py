from sqlalchemy.ext.asyncio import AsyncSession
from src.models.spimex_model import SpimexTradingResults
from src.schemas.trade import TradeResponse
from src.utils.repository import SqlAlchemyRepository
from tests.utils import compare_dicts_and_db_models


class TestSqlAlchemyRepository:
    class _SqlAlchemyRepository(SqlAlchemyRepository):
        model = SpimexTradingResults

    def __get_sql_rep(self, session: AsyncSession) -> SqlAlchemyRepository:
        return self._SqlAlchemyRepository(session)

    async def test_add_one(
        self,
        transaction_session: AsyncSession,
        trade: dict,
        get_trades,
    ) -> None:
        sql_rep = self.__get_sql_rep(transaction_session)
        await sql_rep.add_one(**trade)
        await transaction_session.flush()

        trades_db = await get_trades()
        assert compare_dicts_and_db_models(trades_db, [trade], TradeResponse)
