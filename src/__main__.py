from config import DISCORD_BOT_TOKEN, bot
from cogs.events import Init, SlashCommands, TicketButtons
from cogs.commands import Commands


def main():
    print("program is starting...")

    # add cogs
    bot.add_cog(Init(bot))
    bot.add_cog(SlashCommands(bot))
    bot.add_cog(TicketButtons(bot))
    bot.add_cog(Commands(bot))
    bot.run(DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    main()
