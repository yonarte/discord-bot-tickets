from disnake import Interaction, MessageInteraction, ChannelType, Embed, Colour, ButtonStyle, ui
from disnake.ext import commands

from cogs.views import DialogButtons
from config import logger


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"The bot is ready (name: {self.bot.user.name}; id: {self.bot.user.id})")


class TicketButtons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, inter: MessageInteraction):
        custom_id: str = inter.component.custom_id

        if custom_id == "viewCreateTicket.button.create":
            await inter.response.defer()
            logger.info("Create button pressed...")

            try:
                # Create thread
                thread = await inter.channel.create_thread(
                    name=f"{inter.user.global_name}'s ticket",
                    type=ChannelType.private_thread,
                    invitable=False
                )
                logger.info("Private thread created...")

                # Create message
                embed = Embed(
                    description=f"## New Ticket 🎯\n**Hello** {inter.user.mention}! Your ticket has been succesfully created!\nPlease **describe your issue in detail** and provide any relevant **screenshots** or error **logs**. Our team will assist you as soon as possible!",
                    colour=Colour.green()
                )

                embed.set_footer(
                    text="Use the button below embed to close the ticket!"
                )

                button = ui.Button(
                    style=ButtonStyle.gray,
                    label="Close",
                    custom_id="viewAdminTicket.button.close",
                    emoji="🔒"
                )

                view = ui.View(timeout=None)
                view.add_item(button)

                await thread.add_user(inter.user)
                await thread.send(embed=embed, view=view)
                logger.info("Ticket message sent...")

                # answer message
                answer = Embed(
                    description=f"The [ticket]({thread.jump_url}) has been successfully created!",
                    colour=Colour.green()
                )

                await inter.send(embed=answer, ephemeral=True)
                logger.info("The ticket has been successfully created!")

            except Exception as e:
                text: str = "Failed to create a ticket!"

                answer = Embed(
                    description=text,
                    colour=Colour.red()
                )

                await inter.send(embed=answer, ephemeral=True)
                logger.error(text, exc_info=True)

        elif custom_id == "viewAdminTicket.button.close":
            await inter.response.defer()
            logger.info("Create button pressed...")

            try:
                embed = Embed(
                    description="Are you sure you want to **delete** the ticket?",
                    color=Colour.from_rgb(57, 58, 65)
                )

                view = DialogButtons(inter=inter, timeout=60)

                await inter.send(embed=embed, view=view, ephemeral=True)
                logger.info("Dialog buttons message sent...")

            except Exception as e:
                logger.error("Failed to press close ticket button!", exc_info=True)

