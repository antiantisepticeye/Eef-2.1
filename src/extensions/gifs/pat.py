"""Imports"""

import random
import discord
from discord import app_commands


@app_commands.command(name="pat", description="Pat a user!")
@app_commands.describe(user="The user to give pats", ephemeral="To make the response only visible to you")
async def pat_(interaction:discord.Interaction, user: discord.Member=None, ephemeral:bool=False):
	gifs = [
		"https://media1.tenor.com/images/da8f0e8dd1a7f7db5298bda9cc648a9a/tenor.gif?itemid=12018819",
		"https://media1.tenor.com/images/f5176d4c5cbb776e85af5dcc5eea59be/tenor.gif?itemid=5081286",
		"https://media1.tenor.com/images/6151c42c94df654b1c7de2fdebaa6bd1/tenor.gif?itemid=16456868",
		"https://media1.tenor.com/images/daa885ec8a9cfa4107eb966df05ba260/tenor.gif?itemid=13792462",
		"https://media1.tenor.com/images/55df4c5fb33f3cd05b2f1ac417e050d9/tenor.gif?itemid=6238142",
		"https://media1.tenor.com/images/54722063c802bac30d928db3bf3cc3b4/tenor.gif?itemid=8841561",
		"https://media1.tenor.com/images/005e8df693c0f59e442b0bf95c22d0f5/tenor.gif?itemid=10947495",
		"https://media1.tenor.com/images/5466adf348239fba04c838639525c28a/tenor.gif?itemid=13284057",
		"https://media1.tenor.com/images/1e92c03121c0bd6688d17eef8d275ea7/tenor.gif?itemid=9920853"    
	]
	if user:
		title = f"You gave {user.name} pats"  
	else:
		title = "Have pats :heart:"


	embed= discord.Embed(title=title, color=0x80002f)
	embed.set_image(url=str(random.choice(gifs)))
	await interaction.response.send_message(embed=embed,ephemeral=ephemeral)
   
