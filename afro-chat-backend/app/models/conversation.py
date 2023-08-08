from app.models.user import User
from datetime import datetime
from sqlalchemy import INTEGER, ForeignKey, String, func, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession


class Conversation(Base):
    __tablename__ = "conversation"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    persona: Mapped[str] = mapped_column(String(50), nullable=False)
    system_prompt: Mapped[str] = mapped_column(String(100000), nullable=False)
    total_tokens: Mapped[int] = mapped_column(
        INTEGER, nullable=False, server_default="0"
    )
    created_date: Mapped[datetime] = mapped_column(server_default=func.now())

    messages: Mapped[List["Message"]] = relationship(
        "Message", back_populates="conversation"
    )

    user: Mapped["User"] = relationship("User", back_populates="conversations")

    def __repr__(self):
        return (
            f"<Conversation(id={self.id}, user_id={self.user_id}, persona='{self.persona}', "
            f"system_prompt='{self.system_prompt[:50]}...', total_token={self.total_tokens}, "
            f"created_date={self.created_date})>"
        )

    @classmethod
    async def find(cls, db_session: AsyncSession, id: int):
        """
        :param db_session:
        :param name:
        :return:
        """
        stmt = select(cls).where(cls.id == id)
        result = await db_session.execute(stmt)
        instance: Conversation | None = result.scalars().first()
        return instance


class Message(Base):
    __tablename__ = "message"
    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversation.id"))
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(String(100000), nullable=False)
    token_usage: Mapped[int] = mapped_column(INTEGER, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(server_default=func.now())

    conversation: Mapped["Conversation"] = relationship(
        "Conversation", back_populates="messages"
    )

    def __repr__(self):
        return (
            f"<Message(id={self.id}, conversation_id={self.conversation_id}, role='{self.role}', "
            f"content='{self.content[:50]}...', token_usage={self.token_usage}, "
            f"timestamp={self.timestamp})>"
        )
