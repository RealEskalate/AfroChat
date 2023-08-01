from aiogram import types
import time
from bot.bot_state import State
from .texts import persona_text
from .keyboards import persona_kb
from bot.features.ask.keyboards import ask_keyboard


async def handle_persona_command(message: types.Message):
    try:
        return await message.answer(text=persona_text, reply_markup=persona_kb)
    except Exception:
        return await message.answer(
            text="something\
                happen please came back letter"
        )


async def handle_persona_callback(call: types.CallbackQuery):
    try:
        return await call.message.answer(text=persona_text, reply_markup=persona_kb)
    except Exception:
        return await call.message.answer(
            text="something\
                happen please came back letter"
        )


async def send_formatted_text(message: types.Message):
    # Sending bold text using HTML
    await message.reply(
        "<b>This is bold text using HTML.</b>", parse_mode=types.ParseMode.HTML
    )

    # Sending italic text using HTML
    await message.reply(
        "<i>This is italic text using HTML.</i>", parse_mode=types.ParseMode.HTML
    )

    # Sending strikethrough text using HTML
    await message.reply(
        "<s>This is strikethrough text using HTML.</s>", parse_mode=types.ParseMode.HTML
    )

    # Sending underline text using HTML
    await message.reply(
        "<u>This is underline text using HTML.</u>", parse_mode=types.ParseMode.HTML
    )

    # Sending a code block using HTML
    code_block = "<pre><code>print('Hello, world!')</code></pre>"
    await message.reply(code_block, parse_mode=types.ParseMode.HTML)

    # Sending a link using HTML
    await message.reply(
        "Check out <a href='https://openai.com'>OpenAI</a>!",
        parse_mode=types.ParseMode.HTML,
    )

    # Mentioning a user using HTML
    await message.reply(
        "Hello, <a href='tg://user?id=USER_ID'>@username</a>!",
        parse_mode=types.ParseMode.HTML,
    )

    # Note that not all formatting options are supported in all clients,
    # and the display may vary across different devices and platforms.


async def handle_persona_click_callback(call: types.CallbackQuery):
    try:
        name = call.data.split(":")[1]
        chat_id = str(call.message.chat.id)
        State[chat_id].update({"last_chat": name, "last_request": int(time.time())})

        # formatted_text = """*
        # <b>This is bold</b> text using HTML.
        # <i>This is italic</i> text using HTML.
        # <s>This is strikethrough</s> text using HTML.
        # <u>This is underline</u> text using HTML.
        # <code>inline code</code> using HTML.
        # <pre><code>print('Hello, world!')</code></pre> is a code block using HTML.

        # Check out <a href='https://openai.com'>OpenAI</a> for a link using HTML.

        # Hello, <a href='tg://user?id=USER_ID'>@username</a>! is a mention using HTML."""

        # await call.message.reply(formatted_text, parse_mode=types.ParseMode.HTML)
        return await call.message.reply(
            f"hello {call.message.chat.first_name} I am {name.upper()} How can I help you"
        )
    except Exception:
        return await call.message.answer(
            text="something\
                happen please came back letter"
        )
