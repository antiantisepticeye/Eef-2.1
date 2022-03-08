"""Imports"""

import os
import re
import aiohttp
import discord
from discord import Asset, app_commands
from types import SimpleNamespace
from discord.ext import commands

def asset_from_emoji(state, emoji_id: int, animated=True) -> Asset:
	format = 'gif' if animated else 'png'
	return Asset(
		state,
		url=f'{Asset.BASE}/emojis/{emoji_id}.{format}',
		key=emoji_id,
		animated=animated
	)

@app_commands.command(name="emoji", description="Get an Emoji's info")
@app_commands.describe(emoji="The emoji to get the info for", ephemeral="To make the response only visible to you")
async def emoji_(interaction:discord.Interaction, emoji:str, ephemeral:bool=False):
    try:
        converter = commands.converter.EmojiConverter()

        ctx = SimpleNamespace(bot=interaction.client, guild=interaction.guild)

        emote = await converter.convert(ctx, emoji)

        embed = discord.Embed(title = f"{emote.name}'s Info", description=f"`{emote}`", color=0x80002f, timestamp=emote.created_at)
        embed.set_footer(text="Created at")
        embed.set_image(url=emote.url)
        await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
    except commands.EmojiNotFound:
        try:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://api.eefbot.ga/emojis/parse?argument={emoji}&authKey={os.getenv("API_TOKEN")}') as res:
                        if 200 <= res.status < 300:
                            data = await res.json()
                            if len(data["emoji_data"]):
                                emoji_data = data["emoji_data"][0]
                                embed = discord.Embed(description=f'**{emoji_data["emoji"]} is a Unicode Emoji.**', color=0x80002f)
                                png_url = emoji_data["png"]["twitter"]
                                svg_url = emoji_data["svg"]["discord"]
                                names = emoji_data["names"]

                                embed.set_image(url=png_url)
                                if names:
                                    embed.description += f"\n\n`{', '.join([f':{i}:' for i in names])}`"
                                embed.description += f"\n[svg]({svg_url})"
                                await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
                            else:
                                raise discord.errors.HTTPException(res, "Emoji not found")
                        else:
                            raise discord.errors.HTTPException(res, "Emoji not found")
            
            except discord.errors.HTTPException:
                try:
                    emoji_args =  re.match(r'<(a?):([a-zA-Z0-9\_]{1,32})\\?:([0-9]{15,20})>$', emoji)
                    emoji_args = emoji_args.groups()
                    animated = emoji_args[0] == "a"
                    emoji_name = emoji_args[1]
                    emoji_id = emoji_args[2]
                    emoji_asset = asset_from_emoji(interaction.client._get_state(), emoji_id, animated)

                    embed = discord.Embed(title = f"{emoji_name}'s Info", description=f"**{emoji_name} is an emoji from another guild!**\n`<{'a' if animated else ''}:{emoji_name}:{emoji_id}>`", color=0x80002f)
                    async with aiohttp.ClientSession() as session:
                        async with session.get(emoji_asset.url) as res:
                            if 200 <= res.status < 300:
                                embed.set_image(url=emoji_asset.url)
                                await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
                            else:
                                raise Exception('Couldn\'t fetch emoji')
                    


                except Exception as e:
                    await interaction.client.send_error(interaction, "Emoji not found!", ephemeral=ephemeral)
        except Exception as e:
            print(e)
            await interaction.client.send_error(interaction, "Emoji not found!")
                

