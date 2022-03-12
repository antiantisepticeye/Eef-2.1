"""Imports"""

import datetime
import discord
from discord import app_commands


@app_commands.command(name="user", description="Gets a user's info")
@app_commands.describe(
	user="The user to get the info for",
	ephemeral="To make the response only visible to you"
)
async def user_(interaction:discord.Interaction, user:discord.User, ephemeral:bool=False):
	user: discord.Uer = await interaction.client.fetch_user(user.id)
	guild: discord.Guild = interaction.guild

	member = None
	try: member = await guild.fetch_member(user.id) 
	except discord.errors.NotFound: pass


	is_member = bool(member)
	embed = discord.Embed()
	embed.set_author(name=str(user), icon_url=user.display_avatar.url)
	embed.set_thumbnail(url=user.display_avatar.url)
	embed.color = user.accent_color if user.accent_color else ((member.color if member.color.value else 0x80002f) if is_member else 0x80002f)
	mention_bot = ""
	if user.bot:
		if not user.public_flags.verified_bot:
			mention_bot = "<:bot:878671808096784384>"
		else:
			mention_bot = "<:bot_verified:878686963190861844>"
	embed.description = user.mention + " " + mention_bot
	
	## general stuff
	is_bot = "Yes" if user.bot else "No" 
	user_info_value = ""
	if user.accent_color: user_info_value += f"**Banner Color:** {str(user.accent_color)}\n"
	discord.PublicUserFlags.staff
	badges = {
		"hypesquad": "<:HypeSquad:878714549111500810>",
		"hypesquad_balance": "<:HypeSquad_Balance:878714139957145620>",
		"hypesquad_brilliance": "<:HypeSquad_Brilliance:878713793302118431>",
		"hypesquad_bravery": "<:HypeSquad_Bravery:878713431862161528>",
		"discord_certified_moderator": "<:discord_certified_moderator:878716513459257344>",
	}
	flags = "".join([(badges.get(i[0]) or "") if i[1] else "" for i in user.public_flags])
	if flags: user_info_value += f"**Badges:** {flags}\n"
	user_info_value += f"**Bot:** {is_bot}\n"
	user_info_value += f"**ID:** {user.id}\n"

	embed.add_field(name="User Information", value=user_info_value, inline=True)


	joined_info = "" 
	joined_info += f"**Discord:** <t:{round(user.created_at.timestamp())}:R>\n"
	if is_member: joined_info += f"**Guild:** <t:{round(member.joined_at.timestamp())}:R>\n"
	
	embed.add_field(name="Joined", value=joined_info, inline=True)
	guild_user_info = ""
	if is_member:
		if member.nick: guild_user_info += f"**Nickname:** {member.nick}\n"
		guild_user_info += f"**Roles [{len(member.roles[1:])}]:** {', '.join(reversed([i.mention for i in member.roles[1:]]))}"
		embed.add_field(name="Guild", value=guild_user_info, inline=False)

	if is_member:
		temp_member = member
		status_info = ""
		status_info += "**Mobile: **" if member.is_on_mobile() else "**Desktop: **"
		status_info += temp_member.status.name
		embed.add_field(name="Status", value=status_info, inline=False)
		
		activity_info = ""
		for i in temp_member.activities:
			if type(i) == discord.CustomActivity:
				activity_info += f"**Custom Activity:** {i.name}\n"

			elif type(i) == discord.Activity:
				if i.type == discord.ActivityType.playing: 
					activity_info += f"**Playing:** {i.name}\n"
				
				elif i.type == discord.ActivityType.listening:
					activity_info += f"**Listening:** {i.name}\n"
				
				elif i.type == discord.ActivityType.watching:
					activity_info += f"**Watching:** {i.name}\n"
				



		if activity_info: embed.add_field(name="Activity", value=activity_info, inline=False)
		


	if user.banner: embed.set_image(url=user.banner.url)
	embed.timestamp = datetime.datetime.now()
	await interaction.response.send_message(embed=embed, ephemeral=ephemeral)


