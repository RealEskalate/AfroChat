from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase


from .utils.logger import sqlalchemy_logger as logger
from . import initial_config as config

from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine(
    url=config.POSTGRESS_URL.unicode_string(),
    future=True,
    echo=True,
    pool_size=20,
    max_overflow=20
)

AsyncSessionFactory = sessionmaker(
    engine, autoflush=False, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        logger.debug(f"ASYNC Pool: {engine.pool.status()}")
        yield session
