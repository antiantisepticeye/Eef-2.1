"""Imports"""

import discord
from discord import app_commands



@app_commands.command(name="server_icon", description="Gets the server's icon")
@app_commands.describe(
	ephemeral="To make the response only visible to you"
)
async def server_icon_(interaction: discord.Interaction, ephemeral:bool=False):
	server = interaction.guild
	if server.icon:
		embed = discord.Embed(title=f"**{server.name}**'s icon", color=0x80002f)
		embed.set_image(url=server.icon.url)
		await interaction.response.send_message(embed=embed,ephemeral=ephemeral)
	else: 
		await interaction.client.send_error(interaction, "Server doesn't have an icon!", ephemeral=ephemeral)

