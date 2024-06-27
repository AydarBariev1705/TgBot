from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


from main.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,

    )
    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )
    lastname: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )
