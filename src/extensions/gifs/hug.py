"""Imports"""

import random
import discord
from discord import app_commands


@app_commands.command(name="hug", description="Hug a user!")
@app_commands.describe(
	user="The user to give a hug to",
	ephemeral="To make the response only visible to you"
)
async def hug_(interaction:discord.Interaction, user: discord.Member=None, ephemeral:bool=False):
	gifs = [
		"https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788",
		"https://media1.tenor.com/images/78d3f21a608a4ff0c8a09ec12ffe763d/tenor.gif?itemid=16509980",
		"https://media1.tenor.com/images/9dddcb8d880010200af468d781b4bbcd/tenor.gif?itemid=16831471",
		"https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075",
		"https://media1.tenor.com/images/94989f6312726739893d41231942bb1b/tenor.gif?itemid=14106856",
		"https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587",
		"https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498",
		"https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
		"https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935",
		"https://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705",
		"https://media1.tenor.com/images/5845f40e535e00e753c7931dd77e4896/tenor.gif?itemid=9920978",
		"https://media1.tenor.com/images/f5df55943b64922b6b16aa63d43243a6/tenor.gif?itemid=9375012",
		"https://media1.tenor.com/images/b7487d45af7950bfb3f7027c93aa49b1/tenor.gif?itemid=9882931",
		"https://media1.tenor.com/images/b7487d45af7950bfb3f7027c93aa49b1/tenor.gif?itemid=9882931",
		"https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif?itemid=5044460",
		"https://media1.tenor.com/images/34a1d8c67e7b373de17bbfa5b8d35fc0/tenor.gif?itemid=8995974",
		"https://media1.tenor.com/images/b0de026a12e20137a654b5e2e65e2aed/tenor.gif?itemid=7552093",
		"https://media1.tenor.com/images/42922e87b3ec288b11f59ba7f3cc6393/tenor.gif?itemid=5634630",
		"https://media1.tenor.com/images/d19bfd9ba90422611ec3c2d835363ffc/tenor.gif?itemid=18374323",
		"https://media1.tenor.com/images/aeb42019b0409b98aed663f35b613828/tenor.gif?itemid=14108949",
		"https://media1.tenor.com/images/f855a0348c55a6d0469f34135510bcb2/tenor.gif?itemid=5690234",
		"https://media1.tenor.com/images/e3fea11903891bbb44e1d83040822746/tenor.gif?itemid=14903941",
		"https://media1.tenor.com/images/868514ccca94037608a50a9bd60e69ff/tenor.gif?itemid=13400355"
	]
	if user:
		title = f"I hug you and {user.name} :heart:"  
	else:
		title = "I hug you :heart:"


	embed= discord.Embed(title=title, color=0x80002f)
	embed.set_image(url=str(random.choice(gifs)))
	await interaction.response.send_message(embed=embed,ephemeral=ephemeral)
   
