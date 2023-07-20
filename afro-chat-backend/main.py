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

# def main() -> None:
#     logger1 = logging.getLogger("logger1")
#     # Set the logging level to DEBUG to show all log messages
#     logger1.setLevel(logging.DEBUG)

#     # Create a StreamHandler and set its level to DEBUG
#     file_handler = logging.FileHandler('logs.log', mode='a')
#     file_handler.setLevel(logging.DEBUG)

#     formatter = logging.Formatter(
#         '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)

#     # Add the StreamHandler to the logger
#     logger1.addHandler(file_handler)

#     logger1.debug("this is debug")
#     logger1.warning("this is warning")
#     logger1.critical("this is critical")
#     logger1.info("this is info")
#     logger1.error("this is error")


# if __name__ == "__main__":
#     main()
