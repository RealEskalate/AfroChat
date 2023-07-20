import logging

from config import initial_config as config
from fastapi import Request
from app import create_app

app = create_app(config)


@app.get('/')
async def home(request:Request):
    logger = request.state.logger
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    return {"hello":"world"}

