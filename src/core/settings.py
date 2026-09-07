import logging

from disnake import Intents
from disnake.ext.commands import InteractionBot

from core.config import config


# discord bot
intents: Intents = Intents.all()
intents.message_content = True

bot: InteractionBot = InteractionBot(intents=intents)

# logging
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(config.logs.level)

# add formatter
formatter = logging.Formatter(
    fmt=config.logs.format,
    datefmt=config.logs.datetime
)

# add handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler(filename=config.logs.filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
