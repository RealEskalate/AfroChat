from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Ask, User, Conversation, Message
from app.database import get_db
from typing import List, Optional


async def get_or_create_user(
    telegram_id: str, firstname: str, username: Optional[str] = None
) -> int:
    try:
        async for session in get_db():
            # Check if a User with the given telegram_id exists
            user = await session.execute(
                select(User).where(User.telegram_id == telegram_id)
            )
            user = user.scalar_one_or_none()

            if user is None:
                # If the User does not exist, create a new User
                user = User(
                    telegram_id=telegram_id, firstname=firstname, username=username
                )
                session.add(user)
                await session.commit()

            # Return the id of the User
            return user.id
    except Exception as e:
        raise e


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
        raise e


async def add_new_conversation(conversation: Conversation):
    """
    Add Conversation and get the ID
    """
    try:
        async for session in get_db():
            await conversation.save(session)
            return conversation.id
    except Exception as e:
        raise e


async def add_new_message(
    messages: List[Message],
    conversation_id: int,
    total_tokens: int,
) -> List[Message]:
    """
    add new message to a conversation
    we are assuming that the messages already have conversation_id
    """
    try:
        async for session in get_db():
            conversation = await Conversation.find(session, conversation_id)
            conversation.total_tokens += total_tokens
            session.add_all(messages)
            await session.commit()
            return messages
    except Exception as e:
        raise e


async def get_conversation(
    session_id: int | None, session: AsyncSession
) -> Conversation | None:
    try:
        if not session_id:
            return None
        # async for session in get_db():
        return await Conversation.find(session, session_id)
    except Exception as e:
        raise e
