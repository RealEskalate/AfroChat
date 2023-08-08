from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, select
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.models.base import Base
from sqlalchemy.ext.asyncio import AsyncSession


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[str] = mapped_column(String(50), nullable=False)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[Optional[str]] = mapped_column(String(50))

    conversations: Mapped[List["Conversation"]] = relationship(
        "Conversation", back_populates="user"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.telegram_id!r}, fullname={self.firstname!r})"

    @classmethod
    async def find(cls, db_session: AsyncSession, id: int):
        """
        :param db_session:
        :param name:
        :return:
        """
        stmt = select(cls).where(cls.id == id)
        result = await db_session.execute(stmt)
        instance: User | None = result.scalars().first()
        return instance
