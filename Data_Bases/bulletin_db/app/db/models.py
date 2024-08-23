from sqlalchemy import Integer, BigInteger, Date, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from .database import Base


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
    total: Mapped[int]
    count: Mapped[int]
    date: Mapped[Date]
    created_on: Mapped[Date] = mapped_column(Date, server_default=func.current_date())
    updated_on: Mapped[Date] = mapped_column(Date, onupdate=func.current_date())
