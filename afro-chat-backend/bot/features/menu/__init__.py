from aiogram import Dispatcher
from bot.features.menu.handlers import handle_start_callback, start_handler

def register_main_menu_features(bot : Dispatcher):
    bot.register_message_handler(start_handler, commands=["start"])
    bot.register_callback_query_handler(handle_start_callback, text='start')

