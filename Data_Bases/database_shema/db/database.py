from core.config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass
