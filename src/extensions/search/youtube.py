"""Imports"""

from typing import List, Optional
import discord
from discord import app_commands
import aiohttp

class SearchSelectDropdown(discord.ui.Select):
	def __init__(self, results, id_: int):
		self.id_ = id_
		self.results = results[:9]
		options = [
			discord.SelectOption(label= d.get("title"), value=str(i), description=f'- {d.get("channel", {}).get("title")}', emoji="👉")
			for i, d in enumerate(results)
		]

		super().__init__(placeholder='Choose one of the search results', min_values=1, max_values=1, options=options)

	async def callback(self, interaction: discord.Interaction):
		if interaction.user.id == self.id_:
			await interaction.response.edit_message(embed = result_to_embed(self.results[int(self.values[0])]))

class SearchSelectDropdownView(discord.ui.View):
	def __init__(self, results, id_:int):
		super().__init__()
		self.value = None
		self.add_item(SearchSelectDropdown(results, id_))



def result_to_embed(d) -> discord.Embed:
	embed = discord.Embed(color=0x80002f, url=d.get("link", {}).get("full"))
	video_id = d.get("videoId")
	title = d.get("title")
	thumnail = d.get("thumbnail", {}).get("static", [{}])[0].get("url")
	published = d.get("published", {}).get("simpleText")
	is_live = d.get("is_live")
	channel = d.get("channel", {})
	channel_title = channel.get("title")
	channel_url = channel.get("full_url")
	channel_thumbnail = channel.get("thumbnail", {}).get("url")
	length = d.get("length", {}).get("short")
	views = d.get("viewCount", {})

	if title: embed.title = title
	if video_id: embed.add_field(name="Video ID", value=f"`{video_id}`")
	if thumnail: embed.set_image(url=thumnail)
	if published: 
		embed.add_field(name="Published", value=published)
	if is_live:
		embed.add_field(name="Live", value="Yes")
	if length: embed.add_field(name="Length", value=length)
	if views: 
		if isinstance(views, str):
			embed.add_field(name="Views", value=views)
		else:
			embed.add_field(name="Views", value=views.get("short", {}).get("full"))


	if channel:
		embed.set_footer(text=f"By: {channel_title}", icon_url=channel_thumbnail)
		embed.set_thumbnail(url=channel_thumbnail)

	return embed

def results_to_embed(q, results) -> discord.Embed:
	embed = discord.Embed(color=0x80002f)
	embed.title = f"Results for '{q}':"
	embed.description = ''
	
	for d in results:
		embed.description += f"**[{d.get('title')}]({d.get('link', {}).get('full')})**\n"
		embed.description += f"By: [{d.get('channel', {}).get('title')}]({d.get('channel', {}).get('full_url')})\n\n"

	return embed


@app_commands.command(name="youtube", description="Search a video on youtube")
@app_commands.describe(
	ephemeral="To make the response only visible to you",
	query="The search term to search for"
)
async def youtube_(interaction:discord.Interaction, query:str, ephemeral:bool=False):
	await interaction.response.defer(ephemeral=ephemeral)
	webhook = interaction.followup
	async with aiohttp.ClientSession() as session:
		async with session.get(f"{interaction.client.API_BASE}/search/youtube/video?q={query}&authKey={interaction.client.API_TOKEN}") as res:
			if 200 <= res.status < 300:
				res = await res.json()
				embed = results_to_embed(query, res)
				await webhook.send(embed=embed,ephemeral=ephemeral, view=SearchSelectDropdownView(results=res, id_=interaction.user.id))
			else:
				await interaction.client.send_error(interaction,"Couldn't reach the api", webhook, ephemeral=ephemeral)


async def get_search_suggestions(interaction: discord.Interaction, query:str) -> List[str]:
	results = [query]
	async with aiohttp.ClientSession() as session:
		async with session.get(f'{interaction.client.API_BASE}/search/youtube/autocomplete?q={query}&authKey={interaction.client.API_TOKEN}') as res:
			if 200 <= res.status < 300:
				d = await res.json()
				results = d
	return results

@youtube_.autocomplete('query')
async def command_autocomplete(interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
	results = await get_search_suggestions(interaction, current)
	return [ app_commands.Choice(name=suggestion, value=suggestion) for suggestion in results if suggestion ][:10]