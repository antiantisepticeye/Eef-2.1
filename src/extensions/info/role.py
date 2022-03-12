"""Imports"""

from io import BytesIO
import discord
from discord import app_commands
from cairosvg import svg2png

@app_commands.command(name="role", description="Gets a role's info")
@app_commands.describe(
	role="The role to get the info for",
	ephemeral="To make the response only visible to you"
)
async def role_(interaction:discord.Interaction, role: discord.Role, ephemeral:bool=False):
	try:
		color = role.color if role.color.value else 0x80002f
		
		embed=discord.Embed(color=color, timestamp=role.created_at)
		remove_perms = ['create_instant_invite', 'add_reactions', 'stream',   'read_messages',  'embed_links', 'attach_files',   'read_message_history', 'mute_members',   'deafen_members','external_emojis', 'manage_nicknames', 'connect',   'speak', 'use_voice_activation', 'change_nickname',   'priority_speaker', 'send_tts_messages']
		if role.hoist:
			hoisted = "Yes"
		else:
			hoisted = "No"
		
		if role.mentionable:
			mentionable = "Yes"
		else:
			mentionable = "No"
	

	
		perms = ", ".join(sorted([i[0].title().replace("_", " ") for i in role.permissions if (i[1] and i[0] not in remove_perms)])).replace("Guild", "Server")

		embed.add_field(name="ID", value=f"{role.id}", inline=True)
		embed.add_field(name="Name", value=f"{role.name}", inline=True)
		if str(role.color) == '#000000':
			embed.add_field(name="Color", value="None", inline=True)
		else:
			embed.add_field(name="Color", value=f"{role.color}", inline=True)
		embed.add_field(name="Mention", value=f"`<@&{role.id}>`", inline=True)
		embed.add_field(name="Hoisted", value=f"{hoisted}", inline=True)
		embed.add_field(name="Position", value="28", inline=True)
		embed.add_field(name="Mentionable", value=f"{mentionable}", inline=True) 
		if not role.permissions.administrator:
			if perms: embed.add_field(name="Key Permissions", value=perms, inline=False)
		else:
			embed.add_field(name="Key Permissions", value="Administrator (All permissions)", inline=False)
		if role.icon: embed.set_footer(text="Role Created", icon_url=role.icon)
		else: embed.set_footer(text="Role Created")
		
		if role.color != None:
			svg_code = f"""
			<svg width="257" height="257" viewBox="0 0 257 257" fill="none" xmlns="http://www.w3.org/2000/svg">
			<path fill-rule="evenodd" clip-rule="evenodd" d="M32.9266 24.7772C25.4783 14.893 32.5297 0.75 44.9061 0.75H230.895C236.971 0.75 241.895 5.67487 241.895 11.75V60.9003C241.895 62.0049 241 62.9003 239.895 62.9003H139.475L182.282 119.707C186.309 125.051 186.309 132.415 182.283 137.76L139.464 194.6H239.895C241 194.6 241.895 195.495 241.895 196.6V245.75C241.895 251.825 236.971 256.75 230.895 256.75H44.9119C32.5365 256.75 25.4848 242.609 32.9311 232.724L104.467 137.765C108.493 132.421 108.492 125.056 104.465 119.712L32.9266 24.7772Z" fill="#{str(role.color)[1:]}"/>
			</svg>
			"""
			bytes_ = BytesIO(svg2png(bytestring=svg_code))
			file = discord.File(fp=bytes_, filename="color.png") 
			embed.set_thumbnail(url="attachment://color.png")
		else: file = None
		await interaction.response.send_message(embed=embed, files=[file], ephemeral=ephemeral)
		
	except discord.ext.commands.RoleNotFound:
		await interaction.client.send_error(interaction, "Role not found!", ephemeral=ephemeral)

	
