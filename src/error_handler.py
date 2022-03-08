import discord


async def send_error_embed(interaction:discord.Interaction, error_message:str, webhook: discord.Webhook=None, ephemeral=True):
    embed = discord.Embed(description=f'**{error_message}**', color=0x80002f)
    if not webhook:
        await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
    else:
        await webhook.send(embed=embed, ephemeral=ephemeral)

