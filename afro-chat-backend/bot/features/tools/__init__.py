from aiogram import Dispatcher
from .handlers import handle_tools_command, handle_tools_callback


def register_tool_features(bot: Dispatcher):
    bot.register_callback_query_handler(handle_tools_callback, text="tools")
    bot.register_message_handler(handle_tools_command, commands=["tools"])
