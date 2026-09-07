from cogs.events import Init, TicketButtons
from cogs.commands import Commands

from core.config import config
from core.settings import bot, logger


def main():
    logger.info("Start program...")

    try:
        logger.info("Add cogs...")
        bot.add_cog(Init(bot))
        bot.add_cog(TicketButtons(bot))
        bot.add_cog(Commands(bot))

    except Exception as e:
        logger.error("Failed to add cogs!", exc_info=True)

    bot.run(config.discord_bot.token)


if __name__ == "__main__":
    main()
