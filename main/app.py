from typing import List

from fastapi import FastAPI

from main.database import engine, Base
from main.models import User
from main.shemas import UserOut

app = FastAPI()


@app.on_event("startup")
async def shutdown():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get('/users/', response_model=List[UserOut])
async def get_users() -> List[User]:
    users = await get_users()
    return users

@app.get('/users/{user_id}/', response_model=List[UserOut])
async def get_status(users_id: int):

