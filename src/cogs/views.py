import datetime

from disnake import ui, ButtonStyle, Interaction, MessageInteraction, Embed, Colour


class DialogButtons(ui.View):
    def __init__(self, inter: Interaction, timeout: int):
        super().__init__(timeout=timeout)
        self.inter: Interaction = inter

    async def on_timeout(self) -> None:
        await self.inter.response.defer()
        await self.inter.delete_original_message()

    @ui.button(label="Accept", style=ButtonStyle.green)
    async def buttonAccept(self, button: ui.Button, inter: MessageInteraction):
        await inter.response.defer()
        
        # edit ticket message
        embed: Embed = self.inter.message.embeds[0]
        embed.colour = Colour.red()
        embed.timestamp = datetime.datetime.now()

        embed.set_footer(
            text=f"The ticket has been closed by {inter.user.global_name}"
        ) 

        await self.inter.message.edit(embed=embed, view=None)

        # answer message
        answer = Embed(
            description=f"The ticket has been successfully closed! 🔒",
            colour=Colour.green()
        )

        await inter.followup.edit_message(message_id=inter.message.id, embed=answer, view=None)

        # close thread
        await inter.channel.edit(archived=True, locked=True)

    @ui.button(label="Cancel", style=ButtonStyle.red)
    async def buttonCancel(self, button: ui.Button, inter: MessageInteraction):
        await inter.response.defer()
        await inter.delete_original_message()
