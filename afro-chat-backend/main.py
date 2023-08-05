from config import initial_config as config
from fastapi import Request
from app import create_app, fast_api_logger
from bot.bot import WEBHOOK_URL, WEBHOOK_PATH, dp, bot
from aiogram import Bot, Dispatcher, types

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


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    fast_api_logger.debug(update)
    # print(update, flush=True)
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.get("/")
async def home(request: Request):
    logger = request.state.logger
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    return {"hello": "world"}
