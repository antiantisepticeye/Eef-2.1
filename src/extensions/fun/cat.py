"""Imports"""

import aiohttp
import discord
from discord import app_commands


@app_commands.command(name="cat", description="Get a random picture of a cat")
@app_commands.describe(
	ephemeral="To make the response only visible to you"
)
async def cat_(interaction:discord.Interaction, ephemeral:bool=False):
	await interaction.response.defer(ephemeral=ephemeral)
	webhook = interaction.followup
	async with aiohttp.ClientSession() as session:
		async with session.get("https://aws.random.cat/meow") as res:
			if 200 <= res.status < 300:
				data = await res.json()
				embed = discord.Embed(title="Meow 🐱", color=0x80002f)
				embed.set_image(url=data["file"])

				await webhook.send(embed=embed,ephemeral=ephemeral)
			else:
				await interaction.client.send_error(interaction, "Cat not found!", webhook, ephemeral=ephemeral)

