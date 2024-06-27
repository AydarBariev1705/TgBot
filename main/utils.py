from database import async_session
from sqlalchemy import select
from models import User


async def create_or_update_user(tg_id: int, name: str, lastname: str) -> None:
    """Функция для записи или обновления пользователя в БД"""
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id == tg_id))
        if not user:
            user = User(
                id=tg_id,
                name=name,
                lastname=lastname,
            )
            session.add(user)
            await session.commit()
        elif user:
            user.lastname = lastname
            user.name = name
            await session.commit()


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
