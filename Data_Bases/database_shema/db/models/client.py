from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base


class City(Base):
    __tablename__ = 'city'

    city_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name_city: Mapped[str]
    days_delivery: Mapped[int]

    client_info = relationship('Client', back_populates='city')


class Client(Base):
    __tablename__ = 'client'

    client_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name_client: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey('city.city_id'))
    email: Mapped[str]

    city = relationship('City', back_populates='client_info')

    buy = relationship('Buy', back_populates='client_buy')
