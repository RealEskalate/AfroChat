from sqlalchemy.orm import Mapped, mapped_column, relationship
from database_learn import User
from sqlalchemy import INTEGER, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.models.base import Base


class Ask(Base):
    __tablename__ = 'ask'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    question: Mapped[str] = mapped_column(String(100000), nullable=False)
    answer: Mapped[str] = mapped_column(String(100000), nullable=False)
    token_usage: Mapped[int] = mapped_column(INTEGER, nullable=False)
    user: Mapped['User'] = relationship(backref='user')
