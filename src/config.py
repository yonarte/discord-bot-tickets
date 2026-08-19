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
