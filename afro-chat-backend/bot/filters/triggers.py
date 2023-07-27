from __future__ import annotations
import os

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from config import initial_config

bot_name: str = initial_config.BOT_NAME


class Trigger(BoundFilter):
    def __init__(self, trigger: str | list, args: bool = False):
        self.trigger = trigger.lower() if type(trigger) == str else [
            i.lower() for i in trigger]
        self.args = args

        BoundFilter.__init__(self)

    async def check(self, message: Message):
        try:
            args = message.text.split()
            if args[0].lower() in [f'@{bot_name}', f'{bot_name}']:
                args = args[1:]
            if len(args) == 0:
                return False
            one = ' '.join(args).lower().replace(f'{bot_name}', '').replace('!', '').replace('.', '').\
                replace('/', '').replace('@', '')
            one = one.startswith(self.trigger) if type(
                self.trigger) == str else one.split()[0] in self.trigger
            try:
                two = args[1] if self.args else True
            except:
                two = False
            return one and two
        except:
            return False
