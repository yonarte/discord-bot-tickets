import logging

from disnake import Intents
from disnake.ext import commands

from dotenv import load_dotenv
from os import getenv


# load .env
load_dotenv()
DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")

# discord bot
intents = Intents.all()
intents.message_content = True

bot = commands.InteractionBot(intents=intents)

# logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

FORMAT: str = "[%(asctime)s][%(levelname)s] %(message)s"
DATETIME: str = "%Y.%m.%d %H:%M:%S"

formatter = logging.Formatter(
    fmt=FORMAT,
    datefmt=DATETIME
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler(filename="./bot.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

