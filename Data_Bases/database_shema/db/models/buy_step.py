from sqlalchemy import Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base


class Buy(Base):
    __tablename__ = 'buy'

    buy_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    buy_description: Mapped[str]
    client_id: Mapped[int] = mapped_column(ForeignKey('client.client_id'))

    client_buy = relationship('Client', back_populates='buy')

    buy_step = relationship('BuyStep', back_populates='buy_info')

    buy_book_info = relationship('BuyBook', back_populates='buy_info')


class Step(Base):
    __tablename__ = 'step'

    step_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name_step: Mapped[str]

    buy_step = relationship('BuyStep', back_populates='step_info')


class BuyStep(Base):
    __tablename__ = 'buy_step'

    buy_step_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey('buy.buy_id'))
    step_id: Mapped[int] = mapped_column(ForeignKey('step.step_id'))
    date_step_beg: Mapped[Date] = mapped_column(Date)
    date_step_end: Mapped[Date] = mapped_column(Date)

    buy_info = relationship('Buy', back_populates='buy_step')

    step_info = relationship('Step', back_populates='buy_step')
