from disnake import CommandInteraction, Embed, ButtonStyle, ui, Permissions, Colour
from disnake.ext import commands

from config import logger


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="setup", description="Create category, channel and create ticket message on your server", default_member_permissions=Permissions(administrator=True))
    async def setup(self, inter: CommandInteraction):
        await inter.response.defer(ephemeral=True)
        logger.info(f"'/setup' command used by {inter.user.global_name}...")

        try:
            # Create category and text channel
            categoty = await inter.guild.create_category(
                name="Tickets"
            )
            logger.info("Category created...")

            text_channel = await inter.guild.create_text_channel(
                name="✏️ㆍcreate",
                category=categoty,
                topic="You can create a ticket here!"
            )
            logger.info("Text channel created...")

            # Create message
            container = ui.Container(
                ui.TextDisplay(
                    content=
                        "## Tickets\n" \
                        "1. Click the create button below\n" \
                        "2. Go to the created thread and our team will assist you as soon as possible!"
                ),
                ui.Separator(),
                ui.Section(
                    ui.TextDisplay(content="**New Ticket**\nCreate a private thread with moderators"),
                    accessory=ui.Button(
                        style=ButtonStyle.green,
                        label="Create",
                        custom_id="viewCreateTicket.button.create",
                        emoji="✏️"
                    )
                )
            )

            await text_channel.send(components=[container])
            logger.info("Create ticket message sent...")

            # answer message
            text: str = "The bot has been successfully configured!"

            answer = Embed(
                description=text,
                colour=Colour.green()
            )

            await inter.send(embed=answer, ephemeral=True)
            logger.info(text)

        except Exception as e:
            text: str = "Failed to configure the bot!"
            
            answer = Embed(
                description=text,
                colour=Colour.red()
            )

            await inter.send(embed=answer, ephemeral=True)
            logger.error(text, exc_info=True)
