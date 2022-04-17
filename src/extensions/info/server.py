"""Imports"""

import discord
from discord import app_commands


@app_commands.command(name="server", description="Get the server's info")
@app_commands.describe(
	ephemeral="To make the response only visible to you"
)
async def server_(interaction:discord.Interaction, ephemeral:bool=False):
		guild=interaction.guild
		role_count = len(guild.roles)
		bot_count = 0
		for member in guild.members:
			if member.bot:
				bot_count+=1
		
		embed = discord.Embed(title = f"{guild.name}'s server information", color=0x80002f)
		embed.add_field(name="Owner", value=f"{guild.owner}", inline=True) 
		
		created_at = f"<t:{int(guild.created_at.timestamp())}:F>"

		embed.add_field(name="Created At", value=f"{created_at}", inline=True) 

		embed.add_field(name="Region", value=f"{str(guild.preferred_locale).lower()}", inline=True) 

		embed.add_field(name="Member Count", value=f"{guild.member_count - bot_count}", inline=True) 

		embed.add_field(name="Roles", value=f"{len([role.mention for role in guild.roles]) - 1}", inline=True) 

		embed.add_field(name="Emojis", value=f"{len([emoji.name for emoji in guild.emojis])}", inline=True) 

		embed.add_field(name="Channels", value=f"<:textchannel:835526098603081748> {len(guild.text_channels)} | <:voicechannel:835526343692517446> {len(guild.voice_channels)}", inline=True) 

		try:
			embed.add_field(name="Ban Count", value=f"<:Ban:835528016704700456> {len([i async for i in guild.bans(limit=None)])}", inline=True) 
		except Exception as e:
			print(e)
			pass

		if guild.premium_subscription_count != 0: level = f"(Level {guild.premium_subscription_count})"
		else: level = " "
		
		embed.add_field(name="Boost", value=f"<:Nitro:835529080815878155> {guild.premium_tier} {level}", inline=True) 


		features = "\n".join( [" ".join(i.split('_')) for i in guild.features] ).lower().title()
		if not features: features = "None"
		embed.add_field(name="Features", value=f"{features}", inline=False) 

		embed.add_field(name="Name", value=f"{guild.name}", inline=True) 
		embed.add_field(name="Bots", value=f"{bot_count}", inline=True) 
	
		if guild.description: embed.add_field(name="Description", value=f"{guild.description}", inline=False) 
		
		if guild.scheduled_events:
			events = ""
			for ev in guild.scheduled_events:
				events += f"{ev.name}\t[[link]({ev.create_invite_url()})]" + "\n"

			embed.add_field(name="Scheduled Events", value=events, inline=False)
		
		if guild.icon: embed.set_thumbnail(url=guild.icon.url)
		if guild.banner: embed.set_image(url=guild.banner.url)
		embed.set_footer(text=f"ID: {guild.id}")

		await interaction.response.send_message(embed=embed, ephemeral=ephemeral)


