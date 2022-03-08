"""Imports"""

import aiohttp
import discord
from discord import app_commands


@app_commands.command(name="dog", description="Get a random picture of a dog")
@app_commands.describe(ephemeral="To make the response only visible to you")
async def dog_(interaction:discord.Interaction, ephemeral:bool=False):
    await interaction.response.defer(ephemeral=ephemeral)
    webhook = interaction.followup
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as res:
            if 200 <= res.status < 300:
                data = await res.json()
                embed = discord.Embed(title="Woof! 🥺", color=0x80002f)
                embed.set_image(url=data["message"])

                await webhook.send(embed=embed,ephemeral=ephemeral)
            else:
                await interaction.client.send_error(interaction, "Dog not found!", webhook, ephemeral=ephemeral)

