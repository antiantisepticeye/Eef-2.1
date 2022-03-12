"""Imports"""

import discord
from discord import app_commands



@app_commands.command(name="server_banner", description="Gets the server's banner")
@app_commands.describe(
	ephemeral="To make the response only visible to you"
)
async def server_banner_(interaction: discord.Interaction, ephemeral:bool=False):
	server = interaction.guild
	if server.banner:
		embed = discord.Embed(title=f"**{server.name}**'s banner", color=0x80002f)
		embed.set_image(url=server.banner.url)
		await interaction.response.send_message(embed=embed,ephemeral=ephemeral)
	else: 
		await interaction.client.send_error(interaction, "Server doesn't have a banner!", ephemeral=ephemeral)

