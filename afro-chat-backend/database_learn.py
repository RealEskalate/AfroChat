from aiogram import asyncio
from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, INTEGER, func
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from asyncpg import UniqueViolationError
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from faker import Faker
import random
from datetime import datetime

random.seed(42)

url = "postgresql+asyncpg://root:123456789@localhost/learning_purpose"
engine = create_engine(url, echo=True)


engine = create_async_engine(
    url,
    future=True,
    echo=True,
)

AsyncSessionFactory = sessionmaker(
    engine, autoflush=False, expire_on_commit=False, class_=AsyncSession
)


class Base(DeclarativeBase):
    __name__: str

    # @declared_attr
    # def __tablename__(self) -> str:
    #     return self.__name__.lower()

    async def save(self, db_session: AsyncSession):
        """
        :param db_session:
        :return:

        """
        try:
            db_session.add(self)
            return await db_session.commit()
        except SQLAlchemyError as ex:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex)
            ) from ex

    async def delete(self, db_session: AsyncSession):
        """

        :param db_session:
        :return:
        """
        try:
            await db_session.delete(self)
            await db_session.commit()
            return True
        except SQLAlchemyError as ex:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex)
            ) from ex

    async def update(self, db: AsyncSession, **kwargs):
        """

        :param db:
        :param kwargs
        :return:
        """
        try:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return await db.commit()
        except SQLAlchemyError as ex:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex)
            ) from ex

    async def save_or_update(self, db_session: AsyncSession):
        try:
            db_session.add(self)
            return await db_session.commit()
        except IntegrityError as exception:
            if isinstance(exception.orig, UniqueViolationError):
                return await db_session.merge(self)
            else:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail=repr(exception),
                ) from exception
        finally:
            await db_session.close()


# class User(Base):
#     __tablename__ = "user_account"
#     __mapper_args__ = {"eager_defaults": True}
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]
#     addresses: Mapped[List["Address"]] = relationship(
#         back_populates="user", cascade="all, delete-orphan"
#     )

#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


# class Address(Base):
#     __tablename__ = "address"
#     __mapper_args__ = {"eager_defaults": True}
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")

#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[str] = mapped_column(String(50), nullable=False)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[Optional[str]] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.telegram_id!r}, fullname={self.firstname!r})"


class Ask(Base):
    __tablename__ = "ask"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    question: Mapped[str] = mapped_column(String(1000), nullable=False)
    answer: Mapped[str] = mapped_column(String(1000), nullable=False)

    user: Mapped[User] = relationship(backref="user")


class Conversation(Base):
    __tablename__ = "conversation"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    persona: Mapped[str] = mapped_column(String(50), nullable=False)
    system_propmp: Mapped[str] = mapped_column(String(5000), nullable=False)
    total_token: Mapped[int] = mapped_column(
        INTEGER, nullable=False, server_default="0"
    )
    # created_date: Mapped[datetime] = mapped_column(server_default=func.now())

    messages: Mapped[List["Message"]] = relationship("Message", back_populates="conversation")


class Message(Base):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversation.id"))
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(String(5000), nullable=False)
    token_usage: Mapped[int] = mapped_column(INTEGER, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    conversation: Mapped["Conversation"] = relationship(
        "Conversation", back_populates="messages"
    )


# Dependency
async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        # logger.debug(f"ASYNC Pool: {engine.pool.status()}")
        yield session


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


fake = Faker()

Faker.seed(42)


async def generate_random_users_and_asks(num_users=10, max_asks_per_user=5):
    users = []
    for _ in range(num_users):
        user = User(
            telegram_id=fake.user_name(),
            firstname=fake.first_name(),
            username=fake.user_name()
            if fake.boolean(chance_of_getting_true=50)
            else None,
        )
        # session.add(user)
        users.append(user)

        # users.append(ask)

    async for session in get_db():
        session.add_all(users)
        # session.add_all(asks)
        await session.commit()
    return users


async def generate_asks():
    asks = []
    for _ in range(10):
        ask = Ask(
            user_id=1,
            question=fake.text(max_nb_chars=1000),
            answer=fake.text(max_nb_chars=1000),
        )
        asks.append(ask)

    async for session in get_db():
        session.add_all(asks)
        await session.commit()

    return asks


async def adder(users):
    async for session in get_db():
        session.add_all(users)
        await session.commit()


def fetch_data(session: AsyncSession):
    stm = select(User)
    res = session.scalars(stm)
    for x in res:
        print("---" * 10, x)


# spongebob = User(
#     name="spongebob",
#     fullname="Spongebob Squarepants",
#     addresses=[Address(email_address="spongebob@sqlalchemy.org")],
# )
# sandy = User(
#     name="sandy",
#     fullname="Sandy Cheeks",
#     addresses=[
#         Address(email_address="sandy@sqlalchemy.org"),
#         Address(email_address="sandy@squirrelpower.org"),
#     ],
# )
# patrick = User(name="patrick", fullname="Patrick Star")


# async def main():
#     await init_db()
#     await generate_random_users_and_asks()
# async for session in get_db():
#     session.add_all([spongebob, sandy, patrick])
#     await session.commit()

# asyncio.run(main())
