import time

from disnake import ui, ButtonStyle, Interaction, MessageInteraction, Embed, Colour
from utils import createTicketMessageComponents


class DialogButtons(ui.View):
    def __init__(self, inter: Interaction, timeout: int):
        super().__init__(timeout=timeout)
        self.inter: Interaction = inter

    async def on_timeout(self) -> None:
        await self.inter.response.defer()
        await self.inter.delete_original_message()

    @ui.button(label="Accept", style=ButtonStyle.green)
    async def buttonAccept(self, button: ui.Button, inter: MessageInteraction):
        embed = Embed(
            description=f"The ticket has been successfully closed! 🔒",
            colour=Colour.green()
        )

        components = createTicketMessageComponents(
            author=inter.user,
            colour=Colour.red()
        )

        await self.inter.message.edit(components=components)
        await inter.response.edit_message(embed=embed, view=None)
        await inter.channel.edit(archived=True, locked=True)

    @ui.button(label="Cancel", style=ButtonStyle.red)
    async def buttonCancel(self, button: ui.Button, inter: MessageInteraction):
        await inter.response.defer()
        await inter.delete_original_message()
