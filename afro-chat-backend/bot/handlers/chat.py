import aiogram
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
# from backend.gpt import ask
# from bot.bot import bot
from .. import bot
chat_kb = InlineKeyboardMarkup(row_width=2)
chat_kb.row(InlineKeyboardButton(
    text='💬 Change chat mode', callback_data='start'))

chat_text = '🤖 Hi! This is GPT 3.5 model. How can I assist you today? \n\n <b>Features </b>  \n ⚡️ Instant access'


async def handler_chat_callback(call: CallbackQuery):
    return await call.message.edit_text(text=chat_text, reply_markup=chat_kb)


async def handle_ask(message: Message):
    sent_message = await message.reply("Please wait while I find an answer ❄️...")
    response = "answer for your response"
    # response = await ask(message.text)
    await sent_message.edit_text(response)
