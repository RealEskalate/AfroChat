import logging

from config import initial_config as config
from fastapi import Request
from app import create_app, fast_api_logger

app = create_app(config)


@app.on_event('shutdown')
async def shutdown_event():
    fast_api_logger.info("Shutting down...")


@app.on_event('startup')
async def startup_event():
    fast_api_logger.info("Starting up...")


@app.get('/')
async def home(request: Request):
    logger = request.state.logger
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    return {"hello": "world"}
