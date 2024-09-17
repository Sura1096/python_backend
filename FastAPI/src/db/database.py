from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.core.config import settings

engine = create_async_engine(settings.DB_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)
