from disnake import CommandInteraction, Embed, ButtonStyle, ui, Permissions
from disnake.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="setup", description="Setup the bot for your server", default_member_permissions=Permissions(administrator=True))
    async def setup(self, inter: CommandInteraction):
        await inter.response.defer(ephemeral=True)

        # Create category and text channel
        categoty = await inter.guild.create_category(
            name="Tickets"
        )

        text_channel = await inter.guild.create_text_channel(
            name="✏️ㆍcreate",
            category=categoty,
            topic="You can create a ticket here!"
        )

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

        # send messages
        await text_channel.send(components=[container])
        await inter.send(content="The bot setup successfully", ephemeral=True)
