"""Imports"""

import random
import discord
from discord import app_commands


@app_commands.command(name="bonk", description="Bonk a user!")
@app_commands.describe(user="The user to bonk >:(", ephemeral="To make the response only visible to you")
async def bonk_(interaction:discord.Interaction, user: discord.Member=None, ephemeral:bool=False):
	gifs = [
        "https://media1.tenor.com/images/119ca32322ba24e4ffc4f0d84a6839f1/tenor.gif?itemid=17402810",
        "https://media1.tenor.com/images/79e0ed5c2ed5397fa79f48fccd6265d1/tenor.gif?itemid=20952854",
        "https://media1.tenor.com/images/dc4329d27745a6707219cb658f5b2c46/tenor.gif?itemid=18191826",
        "https://media1.tenor.com/images/544fecdfc2d904cf9b1e36994d3a007d/tenor.gif?itemid=19740955",
        "https://media1.tenor.com/images/ff91dddf9a258a5fff1efdaf709257f9/tenor.gif?itemid=19410756"    
	]
	if user:
		title = f"You bonk {user.name}"
	else:
		title = "I bonked you!"


	embed= discord.Embed(title=title, color=0x80002f)
	embed.set_image(url=str(random.choice(gifs)))
	await interaction.response.send_message(embed=embed,ephemeral=ephemeral)
   
