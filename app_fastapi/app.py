from typing import List, Dict
from fastapi import FastAPI

from app_fastapi.schemas import UserOut

from app_fastapi.database import engine, Base, session
from app_fastapi.models import User
from app_fastapi.utils import get_user, get_users

app = FastAPI()


@app.on_event('startup')
async def shutdown():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event('shutdown')
async def shutdown():
    await session.close()
    await engine.dispose()


@app.get('/users/',
         response_model=List[UserOut]
         )
async def get_users_list() -> List[User]:
    users = await get_users()

    return users


@app.get('/users/{user_id}/',
         response_model=None)
async def get_user_by_id(user_id: int) -> User | Dict:
    user = await get_user(user_id)
    if not user:
        return {'Error': f'User: {user_id} not found'}

    return user
