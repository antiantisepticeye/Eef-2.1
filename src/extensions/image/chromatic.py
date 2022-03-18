"""Imports"""

import discord
from discord import app_commands
from .utils import cv_Image, static_image_content_type
import cv2 


@app_commands.command(name="chromatic", description="make the image chromatic")
@app_commands.describe(
	user="The user who got chromatic",
	image="alternatively select an image",
	strength="how much strength to use",
	no_blur="wether to use blur while adding the effect",
	ephemeral="To make the response only visible to you"
)
async def chromatic_(interaction:discord.Interaction, user: discord.User=None, image: discord.Attachment=None, strength:app_commands.Range[float, 1, 5]=1.5, no_blur:bool=False, ephemeral:bool=False):
	await interaction.response.defer(ephemeral=ephemeral)
	webhook = interaction.followup
	if not user: user = interaction.user
	if image:
		if not image.content_type in static_image_content_type: 
			return await interaction.client.send_error(interaction, "Invalid image type", webhook=webhook, ephemeral=ephemeral)
		url = image.url
	elif user:
		url = user.display_avatar.with_format('png').with_size(256).url
	
	source_image = (await cv_Image.from_url(url)).resize(512, 512)

	embed = discord.Embed(color=0x80002f)
	
	data = cv_Image.chromatic(source_image, strength, no_blur).to_buffer()

	file = discord.File(fp=data, filename="wasted.png")
	embed.set_image(url = "attachment://wasted.png")
	await webhook.send(file=file, embed=embed)
