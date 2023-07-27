import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config import initial_config
from .handlers import start, aboutus, personal, setting, chat
from .filters.triggers import Trigger

API_TOKEN = initial_config.TELEGRAM_BOT_TOKEN

WEBHOOK_PATH = f"/bot/{API_TOKEN}"
SERVICE_URL = f"https://c5f9-196-189-150-186.ngrok-free.app"
WEBHOOK_URL = SERVICE_URL + WEBHOOK_PATH

if not API_TOKEN:
    raise Exception("Telegram API token not found. Set the TELEGRAM_API_TOKEN environment variable.")

bot = Bot(token=API_TOKEN, parse_mode="html")
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


dp.register_message_handler(start.start_handler, commands=["start"])
dp.register_callback_query_handler(start.handle_start_callback, text='start')


dp.register_callback_query_handler(
    personal.handle_list_personal, text_startswith="personals_", state="*"
)
dp.register_message_handler(aboutus.handle_aboutus, Trigger(['about']))
dp.register_callback_query_handler(
    aboutus.handle_aboutus_callback, text="about"
)

dp.register_callback_query_handler(
    setting.handler_setting_callback, text='setting')
dp.register_callback_query_handler(chat.handler_chat_callback, text='chat')
#
# dp.register_message_handler(handle_single_personal,Trigger(['been']))
dp.register_message_handler(chat.handle_ask)
