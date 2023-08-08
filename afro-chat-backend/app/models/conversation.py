from datetime import datetime
from sqlalchemy import DATETIME, INTEGER, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class Conversation(Base):
    __tablename__ = "conversation"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    persona: Mapped[str] = mapped_column(String(50), nullable=False)
    system_propmpt: Mapped[str] = mapped_column(String(5000), nullable=False)
    total_token: Mapped[int] = mapped_column(
        INTEGER, nullable=False, server_default="0"
    )
    created_date: Mapped[datetime] = mapped_column(server_default=func.now())


class Message(Base):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversation.id"))
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(String(5000), nullable=False)
    token_usage: Mapped[int] = mapped_column(INTEGER, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(server_default=func.now())
