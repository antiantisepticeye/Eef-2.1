"""Imports"""

from datetime import datetime
from io import BytesIO
import aiohttp
import discord
from discord import app_commands


@app_commands.command(name="rip", description="Rest in peace 😔")
@app_commands.describe(user="The user who died 😔", ephemeral="To make the response only visible to you")
async def rip_(interaction:discord.Interaction, user: discord.Member, ephemeral:bool=False):
	await interaction.response.defer(ephemeral=ephemeral)
	webhook = interaction.followup
	async with aiohttp.ClientSession() as session:
		async with session.get(f"http://www.tombstonebuilder.com/generate.php?top1=R.I.P.&top2={user.name}'s&top3=hopes%20and%20dreams&top4=({user.created_at.year} - {datetime.now().year})") as res:
			if res.status == 200:

				embed= discord.Embed(title=f"R.I.P. {user.name}", color=0x80002f)
				embed.set_image(url="attachment://rip.png")
				await webhook.send(embed=embed, file=discord.File(fp=BytesIO(await res.read()), filename="rip.png"), ephemeral=ephemeral)
			else:
				interaction.client.send_error(interaction, "Cannot reach the api!", webhook, ephemeral=ephemeral)