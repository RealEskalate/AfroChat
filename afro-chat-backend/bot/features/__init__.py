from aiogram import Dispatcher
from bot.features.ask import register_ask_features
from bot.features.menu import register_main_menu_features
from bot.features.global_handler import register_global_handler
from bot.features.chat import register_chat_features
from bot.features.persona import register_persona_features
from bot.features.tools import register_tool_features


def register_features(bot: Dispatcher):
    register_ask_features(bot)
    register_main_menu_features(bot)
    register_chat_features(bot)
    register_persona_features(bot)
    register_tool_features(bot)
    register_global_handler(bot)
