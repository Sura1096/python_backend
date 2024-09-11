from models.spimex_model import SpimexTradingResults

from .repository import SqlAlchemyRepository


class TradeRepository(SqlAlchemyRepository):
    model = SpimexTradingResults
