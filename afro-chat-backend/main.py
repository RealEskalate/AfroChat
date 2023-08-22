from config import initial_config as config
from fastapi import Request
from app import create_app, fast_api_logger
from bot.bot import WEBHOOK_URL, WEBHOOK_PATH, dp, bot
from aiogram import Bot, Dispatcher, types


def recursive_search(dictionary, target_key) -> dict | None:
    if isinstance(dictionary, dict):
        if target_key in dictionary:
            return dictionary[target_key]
        for key, value in dictionary.items():
            result = recursive_search(value, target_key)

            if result is not None:
                return result
    elif isinstance(dictionary, list):
        for item in dictionary:
            result = recursive_search(item, target_key)
            if result is not None:
                return result
    return None


app = create_app(config)


@app.on_event("shutdown")
async def shutdown_event():
    fast_api_logger.info("Shutting down...")


@app.on_event("startup")
async def startup_event():
    fast_api_logger.info("Starting up...")
    webhook_info = await bot.get_webhook_info()
    fast_api_logger.info(f"webhoo_url : {webhook_info.url}")

    if webhook_info.url != WEBHOOK_URL:
        fast_api_logger.info("Updating the webhook url")
        await bot.set_webhook(url=WEBHOOK_URL)


GROUP_NAME = "@afrochat_discussion"


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    fast_api_logger.debug(update)
    print(update)
    # result: dict | None = recursive_search(update, "from")
    # if result:
    #     user_id: int = result.get("id", None)
    #     if user_id:
    #         state: types.ChatMember = await bot.get_chat_member(GROUP_NAME, user_id)
    #         if state.status == "left":
    #             total_users: int = await bot.get_chat_members_count(GROUP_NAME)
    #             if total_users >= 100:
    #                 return await bot.send_message(chat_id=user_id, text="we are at full capacity right now please cameback after a while")

    #             message_text = f"""Hello! In order to have access to the bot, you need to join our AfroChat Discussion group first.
    #             Please click on this <a href="https://t.me/afrochat_discussion">link</a> or search and join for @afrochat_discussion to join the group and start using the bot.
    #             Thank you😊!"""
    #             return await bot.send_message(chat_id=user_id, text=message_text)

    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    telegram_update = types.Update(**update)
    await dp.process_update(telegram_update)


@app.get("/")
async def home(request: Request):
    logger = request.state.logger
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    return {"hello": "world"}
