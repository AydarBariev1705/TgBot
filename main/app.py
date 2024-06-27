from typing import List

from fastapi import FastAPI

from main.database import engine, Base, session
from main.models import User
from main.shemas import UserOut
from main.utils import get_user

app = FastAPI()


@app.on_event("startup")
async def shutdown():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.get('/users/', response_model=List[UserOut])
async def get_users() -> List[User]:
    users = await get_users()
    return users


@app.get('/users/{user_id}/', response_model=UserOut)
async def get_status(users_id: int):
    user = await get_user(users_id)
    return user
