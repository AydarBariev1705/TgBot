from app_fastapi.database import async_session
from sqlalchemy import select
from app_fastapi.models import User


async def get_users():
    """Функция для извлечения данных о пользователях"""
    async with async_session() as session:
        users = await session.scalars(select(User))
        return users


async def get_user(tg_id: int):
    """Функция для извлечения данных о пользователе"""
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id == tg_id))
        return user
