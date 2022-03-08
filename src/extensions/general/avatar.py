"""Imports"""

import discord
from discord import app_commands



@app_commands.command(name="avatar", description="Gets a user's avatar!")
@app_commands.describe(user="The user whose avatar to get", guild_pfp="To get the guild specific avatar instead", ephemeral="To make the response only visible to you")
async def avatar_(interaction: discord.Interaction, user: discord.Member, guild_pfp: bool=False, ephemeral:bool=False):
	av_user: discord.User = user

	embed = discord.Embed(title = av_user.name)

	if guild_pfp:

		try:
			member = await interaction.guild.fetch_member(av_user.id)
		except discord.errors.NotFound:
			raise discord.errors.MemberNotFound(av_user.id)
		embed.color = av_user.accent_color if av_user.accent_color else ((member.color if member.color.value else 0x80002f) if bool(member) else 0x80002f)
		
		avatar_url = member.guild_avatar
		if not avatar_url:
			await interaction.client.send_error(interaction, "Member does not have a guild avatar!", ephemeral=ephemeral.value)

	else:

		member = None
		try: member = await interaction.guild.fetch_member(av_user.id) 
		except discord.errors.NotFound: pass
		embed.color = av_user.accent_color if av_user.accent_color else ((member.color if member.color.value else 0x80002f) if bool(member) else 0x80002f)

		
		if bool(member):
			if member.guild_avatar:
				embed.description = f"**[guild avatar]({member.guild_avatar.url})**"
		avatar_url = av_user.display_avatar


	embed.set_image(url = avatar_url.url)
	
	
	await interaction.response.send_message(embed=embed, ephemeral=ephemeral)


