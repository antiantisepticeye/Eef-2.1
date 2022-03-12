"""Imports"""

import discord
from discord import app_commands
from .utils import cv_Image
import cv2 


@app_commands.command(name="legofy", description="legofy an image")
@app_commands.describe(
	user="The user to legofy",
	image="alternatively select an image",
	ephemeral="To make the response only visible to you"
)
async def legofy_(interaction:discord.Interaction, user: discord.User=None, image: discord.Attachment=None, ephemeral:bool=False):
	await interaction.response.defer(ephemeral=ephemeral)
	webhook = interaction.followup
	if not user: user = interaction.user
	if image:
		url = image.url 
	elif user:
		url = user.display_avatar.with_format('png').with_size(256).url
	
	source_image = (await cv_Image.from_url(url))
	embed = discord.Embed(color=0x80002f)
	
	data = cv_Image.legofy(source_image).to_buffer()

	file = discord.File(fp=data, filename="wasted.png")
	embed.set_image(url = "attachment://wasted.png")
	await webhook.send(file=file, embed=embed)
