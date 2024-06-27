from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from app_fastapi.config import DATABASE_URL

engine = create_async_engine(url=DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine)
session = async_session()


class Base(AsyncAttrs, DeclarativeBase, ):
    pass
