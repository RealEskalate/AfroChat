from sqlalchemy import select
from app.models import Ask, User
from app.database import get_db
from typing import Optional


async def get_or_create_user(
    telegram_id: str, firstname: str, username: Optional[str] = None
) -> int:
    async for session in get_db():
        # Check if a User with the given telegram_id exists
        user = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = user.scalar_one_or_none()

        if user is None:
            # If the User does not exist, create a new User
            user = User(telegram_id=telegram_id, firstname=firstname, username=username)
            session.add(user)
            await session.commit()

        # Return the id of the User
        return user.id


async def add_question(question: str, answer: str, user_id: int, token_usage):
    try:
        async for session in get_db():
            statement = select(User).where(User.id == user_id)
            user_exists = await session.execute(statement)
            if user_exists:
                ask = Ask(
                    user_id=user_id,
                    question=question,
                    answer=answer,
                    token_usage=token_usage,
                )
                await ask.save(session)
    except Exception as e:
        print("*" * 200)
        print(e)
