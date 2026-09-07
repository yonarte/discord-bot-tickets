from typing import Optional

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv


class DiscordBot(BaseModel):
    token: Optional[str] = None


class AppLogging(BaseModel):
    level: str = "DEBUG"
    format: str = "[%(asctime)s][%(levelname)s] %(message)s"
    datetime: str = "%Y.%m.%d %H:%M:%S"
    filename: str = "././logs/bot.log"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="_",
    )

    discord_bot: DiscordBot = DiscordBot()
    logs: AppLogging = AppLogging()

load_dotenv()
config = Settings()
