"""Imports"""

import discord
from discord import app_commands


@app_commands.command(name="ping", description="Gets the latency of the bot")
@app_commands.describe(ephemeral="To make the response only visible to you")
async def ping_(interaction: discord.Interaction, ephemeral: bool=False):
	ping_latency = round(interaction.client.latency * 1000)
	embed = discord.Embed(color=0x80002f)
	embed.add_field(name=':ping_pong: Ping Pong!', value=f"**{ping_latency} ms**")
	await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
