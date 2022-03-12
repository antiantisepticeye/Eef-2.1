"""Imports"""

import random
import discord
from discord import app_commands


@app_commands.command(name="slap", description="Slap a user!")
@app_commands.describe(
	user="The user to slap",
	ephemeral="To make the response only visible to you"
)
async def slap_(interaction:discord.Interaction, user: discord.Member=None, ephemeral:bool=False):
	gifs = [
		"https://media1.tenor.com/images/d14969a21a96ec46f61770c50fccf24f/tenor.gif?itemid=5509136",
		"https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956",
		"https://media1.tenor.com/images/74db8b0b64e8d539aebebfbb2094ae84/tenor.gif?itemid=15144612",
		"https://media1.tenor.com/images/b7a844cc66ca1c6a4f06c266646d070f/tenor.gif?itemid=17423278",
		"https://media1.tenor.com/images/53d180f129f51575a46b6d3f0f5eeeea/tenor.gif?itemid=5373994",
		"https://cdn.discordapp.com/attachments/728925291644190730/737146559732514956/slap1.gif",
		"https://media1.tenor.com/images/dcd359a74e32bca7197de46a58ec7b72/tenor.gif?itemid=12396060",
		"https://media1.tenor.com/images/92ec42af8364dcc44816a4f2bb1dd0da/tenor.gif?itemid=16881889",
		"https://media1.tenor.com/images/153b2f1bfd3c595c920ce60f1553c5f7/tenor.gif?itemid=10936993",
		"https://media1.tenor.com/images/a66784462f0551c65579e7898ec6be6b/tenor.gif?itemid=20220816",
		"https://media1.tenor.com/images/0892a52155ac70d401126ede4d46ed5e/tenor.gif?itemid=12946466",
		"https://media1.tenor.com/images/bc3d1991d7bec09250e70bd684410b90/tenor.gif?itemid=17897226",
		"https://media1.tenor.com/images/13844a6bc3d247b571e2cee25651d1a1/tenor.gif?itemid=4991177", 
	]
	if user:
		title = f"You slap {user.name}" 
	else:
		title = "I slap you mwahahah!"
	

	embed= discord.Embed(title=title, color=0x80002f)
	embed.set_image(url=str(random.choice(gifs)))
	await interaction.response.send_message(embed=embed,ephemeral=ephemeral)
   
