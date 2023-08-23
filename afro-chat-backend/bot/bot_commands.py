from typing import List
from aiogram.types import BotCommand


BOT_COMMANDS: List[BotCommand] = [
    BotCommand("start", "Open Menu"),
    BotCommand("ask", "Ask me anything"),
    BotCommand("chat", "Start a conversation with Chat-GPT"),
    BotCommand("personas", "Select preferable persona to chat with"),
    BotCommand("tools", "List all our tools"),
]
