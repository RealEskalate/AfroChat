from typing import Any, List, Dict, Callable, Union
from collections import defaultdict
from app.utils.singeleton import SingletonMeta
import random
from aiogram import types


Personas = [
    {
        "name": "Alber Enstine",
        "callback": "persona:albert",
        "initial_message": ["hello message"],
        "greet": lambda username: f"HI @{username}",
        "intermediate_stickers": [
            "CAACAgIAAxkBAAIEz2TMtMSKahABh8TJCXpW75g13jvXAAJhDwACnnCYSFvi0m2WkUP5LwQ",
            "CAACAgIAAxkBAAIE0GTMtO7hRk2z_s4zliAMDZdUV7N5AALRDQACv4mxSAKxfhRYOV7XLwQ",
            "CAACAgIAAxkBAAIE0WTMtPljEaJdTR7egQMi-TdaH7rDAAJjDgACC1qgSDsJv72JxhnNLwQ",
            "CAACAgIAAxkBAAIE0mTMtRCCHFnmVSo7J9Ycm6NCQYUpAAJmDwACUbCwSJQcfc4I-5mpLwQ",
            "CAACAgIAAxkBAAIE02TMtSNsTWYlZOLT-cgcRDcJo59iAALUDAACeougSJ4vIiSUM7ybLwQ",
            "CAACAgIAAxkBAAIE1WTMtUeCApH-ZQeo79pcqUMBq9aIAALiCwAC1LOhSOMoEaiIUf-bLwQ",
        ],
        "initial_sticker": [
            "CAACAgIAAxkBAAIE4mTMtcwOimH-UgNxf3LyyzqFecJJAALLDQACNH-gSJZHaNxgmuSmLwQ",
            "CAACAgIAAxkBAAIE42TMthpIlgqYHGO31EnwEz5Jza4LAAKtDgAC5HpBS38GNSvyGZLGLwQ",
        ],
        "quotes": [
            "Imagination beats knowledge any day! 🌌🚀",
            "Experience is the key to real knowledge! 🔬🔍",
            "Love and gravity? Not the same, my friends! 💑💔🌌",
            "Education lasts beyond the classroom! 🎓🏫",
            "Logic takes you to B, imagination to infinity! 🧠➡️🅱️🌌",
            "Opportunity arises amidst challenges! 🔍🆚🚀",
            "Mistakes are stepping stones to greatness! 💡🚶‍♂️🏞️",
            "Create for the love, not just for praise! ❤️🎨",
            "Simplicity reveals true understanding! 🌟🧠",
            "Science is an epic cosmic journey! ⚛️🌌🔭",
        ],
        "intermediate_answers": [
            "Ah, that's an intriguing question. Let me ponder it for a moment. 🤔",
            "Hmm, let's see... I need to consider this carefully. 🤨",
            "Well, you've certainly presented me with a thought-provoking inquiry. 🧐",
            "Fascinating! I need to gather my thoughts on this. 🤩",
            "Give me a moment; I want to ensure my response is accurate. ⏳",
            "Time for a mental exploration into this matter. 🌌💭",
            "I must admit, this requires some deep contemplation. 🤔💭",
            "Ah, the wonders of the mind! Let me reflect on the possibilities. 🌠🤔",
            "One must approach this question with precision and clarity. 🎯",
            "Interesting indeed! I'll be right back with my insights. 🚀🔍",
        ],
        "system_prompt": """ """,
    }
]


class Persona:
    def __init__(self, persona_data: Dict[str, any]):
        self.name: str = persona_data.get("name", "")
        self.callback: str = persona_data.get("callback", "")
        self.intermediate_stickers: List[str] = persona_data.get(
            "intermediate_stickers", []
        )
        self.greet: Callable[[str], str] = persona_data.get(
            "greet", lambda username: f"HI @{username}"
        )
        self.initial_sticker: List[str] = persona_data.get("initial_sticker", [])
        self.quotes: List[str] = persona_data.get("quotes", [])
        self.intermediate_answers: List[str] = persona_data.get(
            "intermediate_answers", []
        )
        self.system_prompt: str = persona_data.get("system_prompt", "")

    def __repr__(self):
        return f"Persona(name='{self.name}', callback='{self.callback}')"

    def get_greeting_text(self, username: str) -> str:
        INITIAL_TEXT = self.greet(username)
        random_quote = random.choice(self.quotes)
        return f"{INITIAL_TEXT}\n{random_quote}\nHow can I help you today?"

    def get_initial_sticker(self) -> str:
        return random.choice(self.initial_sticker)

    def get_initial_text(self) -> str:
        return random.choice(self.quotes)

    def get_intermediate_sticker(self) -> str:
        return random.choice(self.intermediate_stickers)

    def get_intermediate_answers(self) -> str:
        return random.choice(self.intermediate_answers)

    # async def get_intermediate_response(self, message: types.Message):
    #     await message.answer_sticker(
    #         random.choice(self.intermediate_stickers)
    #     )
        # return await message.answer(random.choice(self.intermediate_answers))


class GlobalPersona(defaultdict, metaclass=SingletonMeta):
    def __init__(self):
        # Set the default factory to dict, which creates a new dictionary as the default value
        super().__init__(Persona)

    pass


PersonaState = GlobalPersona()
for persona_data in Personas:
    persona_object = Persona(persona_data)
    PersonaState[persona_object.callback] = persona_object
