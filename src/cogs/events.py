import time

from disnake import Interaction, MessageInteraction, ChannelType, Embed, Colour, ButtonStyle, ui
from disnake.ext import commands

from utils import createTicketMessageComponents
from cogs.views import DialogButtons


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # log bot info here
        print(f"[START] name: {self.bot.user.name}#{self.bot.user.id}")


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: Interaction, error):
        # log slash command errors here
        print(f"[ERROR] {error}")


class TicketButtons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, inter: MessageInteraction):
        custom_id: str = inter.component.custom_id

        if custom_id == "viewCreateTicket.button.create":
            # Create thread
            thread = await inter.channel.create_thread(
                name=f"{inter.user.global_name}'s ticket",
                type=ChannelType.private_thread,
                invitable=False
            )

            # Create message
            components = createTicketMessageComponents(
                author=inter.user,
                colour=Colour.green()
            )

            await thread.send(components=components)

            embed = Embed(
                description=f"The [ticket]({thread.jump_url}) has been successfully created!",
                colour=Colour.green()
            )

            await inter.send(embed=embed, ephemeral=True)

        elif custom_id == "viewAdminTicket.button.close":
            embed = Embed(
                description="Are you sure you want to **delete** the ticket?",
                color=Colour.from_rgb(57, 58, 65)
            )

            view = DialogButtons(inter=inter, timeout=60)

            await inter.send(embed=embed, view=view, ephemeral=True)
