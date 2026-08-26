from disnake import Interaction, MessageInteraction, ChannelType, Embed, Color, ButtonStyle, ui
from disnake.ext import commands

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
                type=ChannelType.private_thread
            )

            await thread.add_user(inter.user)

            # Create message
            container = ui.Container(
                ui.TextDisplay(content="## New ticket\nDescribe your issue or question here and moderators will help you!"),
                ui.Separator(),
                ui.TextDisplay(content=f"`👤Author`\n{inter.user.mention}"),
                ui.TextDisplay(content="`🗂️Category`\n**Base ticket**"),
                ui.TextDisplay(content="`📊Status`\n**Active**"),
                ui.Separator(),
                ui.ActionRow(
                    ui.Button(
                        style=ButtonStyle.gray,
                        label="Category",
                        disabled=True,  # Add func later
                        custom_id="viewAdminTicket.button.category",
                        emoji="🗂️"
                    ),
                    ui.Button(
                        style=ButtonStyle.gray,
                        label="Status",
                        disabled=True,  # Add func later
                        custom_id="viewAdminTicket.button.status",
                        emoji="🧷"
                    ),
                    ui.Button(
                        style=ButtonStyle.red,
                        label="Close",
                        custom_id="viewAdminTicket.button.close",
                        emoji="📌"
                    )
                )
            )
            
            await thread.send(components=[container])

            embed = Embed(
                description=f"The [ticket]({thread.jump_url}) has been successfully created!",
                colour=Color.green()
            )

            await inter.send(embed=embed, ephemeral=True)

        elif custom_id == "viewAdminTicket.button.close":
            embed = Embed(
                description="Are you sure you want to **delete** the ticket?",
                color=Color.from_rgb(57, 58, 65)
            )

            view = DialogButtons(inter=inter, timeout=60)

            await inter.send(embed=embed, view=view, ephemeral=True)
