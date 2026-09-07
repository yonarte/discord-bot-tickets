from typing import Optional
from os import getenv

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv


load_dotenv()


class DiscordBot(BaseModel):
    # token: Optional[str] = None
    token: Optional[str] = getenv("DISCORD_BOT_TOKEN")


class AppLogging(BaseModel):
    level: str = "DEBUG"
    format: str = "[%(asctime)s][%(levelname)s] %(message)s"
    datetime: str = "%Y.%m.%d %H:%M:%S"
    filename: str = "././logs/bot.log"


class Settings(BaseSettings):
    # load .env is not working now...
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="_",
    )
    """

    discord_bot: DiscordBot = DiscordBot()
    logs: AppLogging = AppLogging()

config = Settings()
