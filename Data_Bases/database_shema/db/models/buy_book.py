from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base


class BuyBook(Base):
    __tablename__ = 'buy_book'

    buy_book_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey('buy.buy_id'))
    book_id: Mapped[int] = mapped_column(ForeignKey('book.book_id'))
    amount: Mapped[int]

    buy_info = relationship('Buy', back_populates='buy_book_info')
    book_info = relationship('Book', back_populates='buy_book_info')
