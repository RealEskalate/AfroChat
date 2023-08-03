import aiohttp
from typing import List, Tuple
import ujson
import asyncio

from app.database_operations import add_question


async def make_request(messages: List[dict[str, str]]) -> Tuple[str, int]:
    url = "https://api.openai.com/v1/chat/completions"

    payload = ujson.dumps(
        {"model": "gpt-3.5-turbo-16k", "messages": messages, "temperature": 0.3}
    )

    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=payload, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    answer = data["choices"][0]["message"]["content"]
                    total_tokens = data["usage"]["total_tokens"]
                    return answer, total_tokens
                else:
                    raise Exception(
                        f"Request failed with status code {response.status} error : {await response.text()}"
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
    answer, total_tokens = await make_request(messages)

    asyncio.create_task(add_question(
        question=question, answer=answer, user_id=user_id, token_usage=total_tokens
    ))
    return answer
