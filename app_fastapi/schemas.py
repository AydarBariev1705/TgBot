from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int
    name: str
    lastname: str


class UserIn(BaseUser):
    ...


class UserOut(BaseUser):
    id: int

