from aiogram import Bot, Dispatcher
from config import initial_config

from bot.features import register_features


API_TOKEN = initial_config.TELEGRAM_BOT_TOKEN

WEBHOOK_PATH = f"/bot/{API_TOKEN}"
SERVICE_URL = "https://1d8b-185-177-124-201.ngrok-free.app"
WEBHOOK_URL = SERVICE_URL + WEBHOOK_PATH

if not API_TOKEN:
    raise Exception(
        "Telegram API token not found.\
        Set the TELEGRAM_API_TOKEN environment variable."
    )

bot = Bot(token=API_TOKEN, parse_mode="html")
dp = Dispatcher(bot)
register_features(dp)


# dp.register_message_handler(start.start_handler, commands=["start"])
# dp.register_callback_query_handler(start.handle_start_callback, text='start')

# @dp.message_handler(commands=['start','help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """

#
#     user = types.User.get_current()
#     bot = Bot.get_current()
#     bot.ban_chat_member
#     await bot.send_message(user.id,text="this is the message")
#     await message.reply(f"Hi {user.mention}!\nI'm EchoBot!\nPowered by aiogram.")

# dp.register_callback_query_handler(
#     personal.handle_list_personal, text_startswith="personals_", state="*"
# )
# dp.register_message_handler(aboutus.handle_aboutus, Trigger(['about']))
# dp.register_callback_query_handler(
#     aboutus.handle_aboutus_callback, text="about"
# )

# dp.register_callback_query_handler(
#     setting.handler_setting_callback, text='setting')
# dp.register_callback_query_handler(chat.handler_chat_callback, text='chat')
# dp.register_callback_query_handler(chat.handler_chat_callback, text='ask')
# dp.register_message_handler(handle_single_personal,Trigger(['been']))
# dp.register_message_handler(chat.handle_ask)