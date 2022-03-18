"""Imports"""

import discord
from discord import app_commands
from .utils import cv_Image, static_image_content_type
import cv2 


@app_commands.command(name="wanted", description="wanted!")
@app_commands.describe(
	user="The user who is wanted",
	image="alternatively select an image",
	ephemeral="To make the response only visible to you"
)
async def wanted_(interaction:discord.Interaction, user: discord.User=None, image: discord.Attachment=None, ephemeral:bool=False):
	await interaction.response.defer(ephemeral=ephemeral)
	webhook = interaction.followup
	if not user: user = interaction.user
	if image:
		if not image.content_type in static_image_content_type: 
			return await interaction.client.send_error(interaction, "Invalid image type", webhook=webhook, ephemeral=ephemeral)
		url = image.url 
	elif user:
		url = user.display_avatar.with_format('png').with_size(256).url
	
	source_image = (await cv_Image.from_url(url)).greyscale().resize(722, 738)
	poster_image = cv_Image.from_asset("wanted")
	res_image = poster_image.paste(source_image, 134, 421, filter_="multiply")
	embed = discord.Embed(color=0x80002f)
	
	data = res_image.to_buffer()

	file = discord.File(fp=data, filename="wasted.png")
	embed.set_image(url = "attachment://wasted.png")
	await webhook.send(file=file, embed=embed)
