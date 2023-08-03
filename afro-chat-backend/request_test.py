import aiohttp
import asyncio
from typing import Tuple

import ujson


async def make_request(question: str) -> Tuple[str, int]:
    url = "https://api.openai.com/v1/chat/completions"
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant and your name is AfroChat made by A2SV",
        },
        {"role": "user", "content": question},
    ]

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


async def main():
    answer, token_usage = await make_request("who are you")
    print(answer, token_usage)


asyncio.run(main())
