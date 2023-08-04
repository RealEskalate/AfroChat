from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


persona_cb = CallbackData('persona', 'name')

persona_kb = InlineKeyboardMarkup(row_width=2)

persona_kb.insert(InlineKeyboardButton(text="Albert Einstein", callback_data=persona_cb.new('albert')))
persona_kb.insert(InlineKeyboardButton(text="Bill Gates", callback_data=persona_cb.new('sami')))
persona_kb.insert(InlineKeyboardButton(text="Kevin Hart", callback_data=persona_cb.new('birook')))
persona_kb.insert(InlineKeyboardButton(text="Nelson Mandela", callback_data=persona_cb.new('eyu')))
persona_kb.row(InlineKeyboardButton(
    text='🔙 Go Back to Main Menu', callback_data='start'))
