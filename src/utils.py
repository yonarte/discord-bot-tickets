from disnake import ui, Member, ButtonStyle, Colour
from typing import Any


def createTicketMessageComponents(author: Member, created_at: int, colour: Colour) -> Any:
    components = [
        ui.Container(
            ui.TextDisplay(content=f"## New Ticket 🎯\n**Hello** {author.mention}! Your ticket has been succesfully created. Please describe your issue in **detail** and provide any relevant **screenshots** or error **logs**. Our team will assist you **as soon as possible!**"),
            ui.Separator(),
            ui.TextDisplay(content=f"📝 **Description:**\n```Ticket's description here```"),
            ui.Separator(),
            ui.ActionRow(
                ui.Button(
                    style=ButtonStyle.gray,
                    label="Edit",
                    custom_id="viewAdminTicket.button.status",
                    emoji="⚙️"
                ),
                ui.Button(
                    style=ButtonStyle.red,
                    label="Close",
                    custom_id="viewAdminTicket.button.close",
                    emoji="🔒"
                )
            ),
            accent_colour=colour
        )
    ]

    return components
