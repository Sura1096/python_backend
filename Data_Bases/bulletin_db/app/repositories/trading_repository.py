from db.models import SpimexTradingResults
from repositories.base_repository import TradingRepo


class TradingRepository(TradingRepo):
    model = SpimexTradingResults
