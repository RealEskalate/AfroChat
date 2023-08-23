from datetime import datetime
import aiohttp
from typing import List, Tuple
from sqlalchemy import select
import ujson
import asyncio
from app.models import Conversation, Message
from bot.features import persona
from config import initial_config
from app.database_operations import (
    add_new_message,
    add_question,
    add_new_conversation,
    get_conversation,
)
from database_learn import get_db


async def make_request(messages: List[dict[str, str]]) -> Tuple[str, int, int, int]:
    url = "https://api.openai.com/v1/chat/completions"

    payload = ujson.dumps(
        {"model": "gpt-3.5-turbo", "messages": messages, "temperature": 0.1}
    )

    headers = {
        "Authorization": f"Bearer {initial_config.OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=payload, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    answer = data["choices"][0]["message"]["content"]
                    total_tokens = data["usage"]["total_tokens"]
                    prompt_tokens = data["usage"]["prompt_tokens"]
                    completion_tokens = data["usage"]["completion_tokens"]
                    return answer, prompt_tokens, completion_tokens, total_tokens
                else:
                    raise Exception(
                        f"Request failed with status code {response.status}\
                                error : {await response.text()}",
                    )
    except Exception as e:
        # Handle the exception here other exceptions here
        raise Exception(f"Request failed {str(e)}")


async def make_ask_request(question: str, user_id: int):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant and your name is AfroChat made by A2SV",
        },
        {"role": "user", "content": question},
    ]
    answer, _, _, total_tokens = await make_request(messages)

    asyncio.create_task(
        add_question(
            question=question, answer=answer, user_id=user_id, token_usage=total_tokens
        )
    )
    return answer


async def make_chat_request(
    history: List[dict[str, str]],
    system_prompt: str,
    question: str,
    user_id: int,
    persona: str,
    session_id: int | None,
) -> Tuple[dict[str, str], int]:
    try:
        # prepare a messages array that is list of dicts
        messages: List[dict[str, str]] = []
        # add the system prompt at the begginging
        messages.append(
            {
                "role": "system",
                "content": system_prompt,
            }
        )
        # add the history
        messages.extend(history)

        # add the new quesiont
        messages.append({"role": "user", "content": question})

        # perform a request
        response, prompt_tokens, completion_tokens, total_tokens = await make_request(
            messages
        )

        # if session id is none it means it is a new conversation so create a new session and save it

        if session_id is None:
            # create a new Conversation object
            conversation = Conversation(
                user_id=user_id,
                persona=persona,
                system_prompt=system_prompt,
                total_tokens=total_tokens,
                created_date=datetime.utcnow(),
            )
            conversation.messages.append(
                Message(
                    role="user",
                    content=question,
                    token_usage=prompt_tokens,
                    timestamp=datetime.utcnow(),
                )
            )
            conversation.messages.append(
                Message(
                    role="assistant",
                    content=response,
                    token_usage=completion_tokens,
                    timestamp=datetime.utcnow(),
                )
            )

            session_id = await add_new_conversation(conversation)
        else:
            temp_messages: List[Message] = [
                Message(
                    conversation_id=session_id,
                    role="user",
                    content=question,
                    token_usage=prompt_tokens,
                    timestamp=datetime.utcnow(),
                ),
                Message(
                    conversation_id=session_id,
                    role="assistant",
                    content=response,
                    token_usage=completion_tokens,
                    timestamp=datetime.utcnow(),
                ),
            ]

            asyncio.create_task(
                add_new_message(
                    temp_messages, conversation_id=session_id, total_tokens=total_tokens
                )
            )

            # add the messages here

        messages.append({"role": "assistant", "content": response})

        return messages[-1], session_id
    except Exception as e:
        raise e
