from aiogram import Bot, Dispatcher, types
from config import initial_config

from app.bot.features import register_features


API_TOKEN = initial_config.TELEGRAM_BOT_TOKEN

WEBHOOK_PATH = f"/bot/{API_TOKEN}"
SERVICE_URL = "https://afrochat-bot-telegram-ij7jnmwh2q-zf.a.run.app"
WEBHOOK_URL = SERVICE_URL + WEBHOOK_PATH


if not API_TOKEN:
    raise Exception(
        "Telegram API token not found.\
        Set the TELEGRAM_API_TOKEN environment variable."
    )

bot = Bot(token=API_TOKEN, parse_mode="html")
dp = Dispatcher(bot)


register_features(dp)
