"""Imports"""

import random
import discord
from discord import app_commands


@app_commands.command(name="choose", description="Chooses randomly from the options")
@app_commands.describe(ephemeral="To make the response only visible to you")
async def choose_(interaction:discord.Interaction,
	option1: str = None,
	option2: str = None,
	option3: str = None,
	option4: str = None,
	option5: str = None,
	option6: str = None,
	option7: str = None,
	option8: str = None,
	option9: str = None,
	option10: str = None,
	ephemeral:bool=False):
	options = [option1, option2, option3, option4, option5, option6, option7, option8, option9, option10]
	options = [i for i in options if i]

	result_option = random.choice(options)

	description = "From\n" + ",\n".join([f"{i+1}. {n}" for (i, n) in enumerate(options)]) + "\n\n" + f"I choose `{result_option}`"
	embed = discord.Embed(description=f"**{description}**", color=0x80002f)
	await interaction.response.send_message(embed=embed, ephemeral=ephemeral)

	