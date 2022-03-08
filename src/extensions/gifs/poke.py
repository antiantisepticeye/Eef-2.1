"""Imports"""

import random
import discord
from discord import app_commands


@app_commands.command(name="poke", description="Poke a user!")
@app_commands.describe(user="The user you wanna poke", ephemeral="To make the response only visible to you")
async def poke_(interaction:discord.Interaction, user: discord.Member=None, ephemeral:bool=False):
	gifs = [
		"https://media1.tenor.com/images/0da232de2ee45e1464bf1d5916869a39/tenor.gif?itemid=16935454",
		"https://media1.tenor.com/images/e8b25e7d069c203ea7f01989f2a0af59/tenor.gif?itemid=12011027",
		"https://media1.tenor.com/images/01b264dc057eff2d0ee6869e9ed514c1/tenor.gif?itemid=14346763",
		"https://media1.tenor.com/images/cbf38a2e97a348a621207c967a77628a/tenor.gif?itemid=6287077",
		"https://media1.tenor.com/images/963e4620c8b6345f09d7d22ef1c91420/tenor.gif?itemid=12045584",
		"https://media1.tenor.com/images/e8e15ece5fe1b91e8d349402b8fe1fad/tenor.gif?itemid=16935453",
		"https://media1.tenor.com/images/decc2c2f705b74556142d4b746c2dc97/tenor.gif?itemid=12016340",
		"https://media1.tenor.com/images/1b030d975ca0a44b63b53a5ec81696ed/tenor.gif?itemid=19326800",
	]
	if user:
		title = f"You poke {user.name} hehe"  
	else:
		title = "I poke you"


	embed= discord.Embed(title=title, color=0x80002f)
	embed.set_image(url=str(random.choice(gifs)))
	await interaction.response.send_message(embed=embed,ephemeral=ephemeral)
   
