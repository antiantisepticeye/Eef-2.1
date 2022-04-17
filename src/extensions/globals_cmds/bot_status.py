"""Imports"""

import platform
import discord
from discord import app_commands
from utils.neofetch import neofetch


@app_commands.command(name="bot_status", description="Gets the status of the bot")
@app_commands.describe(
	ephemeral="To make the response only visible to you"
)
async def bot_status_(interaction: discord.Interaction, ephemeral: bool=False):
	embed = discord.Embed(color=0x80002f)
	embed.description = neofetch(interaction)
	await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
