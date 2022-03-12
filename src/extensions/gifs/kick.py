"""Imports"""

import random
import discord
from discord import app_commands


@app_commands.command(name="kick", description="Kick a user!")
@app_commands.describe(
	user="The user to kick",
	ephemeral="To make the response only visible to you"
)
async def kick_(interaction:discord.Interaction, user: discord.Member=None, ephemeral:bool=False):
	gifs = [
		"https://media1.tenor.com/images/fb2a19c9b689123e6254ad9ac6719e96/tenor.gif?itemid=4922649",
		"https://media1.tenor.com/images/ea2c3b49edf2080e0ef2a2325ddb4381/tenor.gif?itemid=14835708",
		"https://media1.tenor.com/images/1071791f88205a82dfc4448f08a6b25c/tenor.gif?itemid=17562086",
		"https://media1.tenor.com/images/2ce5a017f6556ff103bce87b273b89b7/tenor.gif?itemid=16407803",
		"https://media1.tenor.com/images/15a74d10bb6dce11476acfdefe614540/tenor.gif?itemid=7779674",
		"https://media1.tenor.com/images/c7e62a49f58c8e4a69b0e613d26b6f34/tenor.gif?itemid=10241448",
		"https://media1.tenor.com/images/b98401fb2a6981c05b064bf7ec148482/tenor.gif?itemid=16419384",
		"https://media1.tenor.com/images/7ad8cdd67a2937de54a75e7858f430c6/tenor.gif?itemid=19326658",
	]
	if user:
		title = f"you kicked {user.name} oof"  
	else:
		title = "A kick! Ha!"


	embed= discord.Embed(title=title, color=0x80002f)
	embed.set_image(url=str(random.choice(gifs)))
	await interaction.response.send_message(embed=embed,ephemeral=ephemeral)
   
