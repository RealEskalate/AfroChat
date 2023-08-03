from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.models.base import Base


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[str] = mapped_column(String(50), nullable=False)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[Optional[str]] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.telegram_id!r}, fullname={self.firstname!r})"
