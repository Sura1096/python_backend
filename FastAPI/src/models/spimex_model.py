from datetime import date

from sqlalchemy import BigInteger, Date, Integer, func
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.schemas.trade import TradeResponse


class SpimexTradingResults(Base):
    __tablename__ = 'spimex_trading_results'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    exchange_product_id: Mapped[str]
    exchange_product_name: Mapped[str]
    oil_id: Mapped[str]
    delivery_basis_id: Mapped[str]
    delivery_basis_name: Mapped[str]
    delivery_type_id: Mapped[str]
    volume: Mapped[int]
    total: Mapped[int] = mapped_column(BigInteger)
    count: Mapped[int]
    date: Mapped[date]
    created_on: Mapped[date] = mapped_column(Date, server_default=func.current_date())
    updated_on: Mapped[date] = mapped_column(Date, onupdate=func.current_date())

    def to_pydantic_schema(self) -> TradeResponse:
        return TradeResponse(**self.__dict__)
