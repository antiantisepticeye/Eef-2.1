"""Imports"""

import discord
from discord import app_commands


from typing import List, Tuple
from utils.fuzzy_search import fuzzy_search 
import discord

from ..general import General
from ..fun import Fun
from ..info import Info
from ..gifs import Gifs
 

embed1 = discord.Embed(title="Eef Hellp", description="```Use the command option to get more info on a specific command```", color=0x80002f)
gen_cmds = General._children.keys()
embed1.add_field(name="General commands", value=",\n".join(gen_cmds))

embed2 = discord.Embed(title="Eef Hellp", description="```Use the command option to get more info on a specific command```", color=0x80002f)
fun_cmds = Fun._children.keys()
embed2.add_field(name="🎉 Fun commands", value=",\n".join(fun_cmds))

embed3 = discord.Embed(title="Eef Hellp", description="```Use the command option to get more info on a specific command```", color=0x80002f)
info_cmds = Info._children.keys()
embed3.add_field(name="ℹ Info commands", value=",\n".join(info_cmds))

embed4 = discord.Embed(title="Eef Hellp", description="```Use the command option to get more info on a specific command```", color=0x80002f)
gif_cmds = Gifs._children.keys()
embed4.add_field(name="😎 Gif commands", value=",\n".join(info_cmds))


help_embeds = {
	"embed1": embed1,
	"embed2": embed2,
	"embed3": embed3,
	"embed4": embed4
	}

class Dropdown(discord.ui.Select):
	def __init__(self, id_:int):
		self.id_ = id_

		options = [
			discord.SelectOption(label='General', value="embed1", description='General command list', emoji=u'\u2139'),
			discord.SelectOption(label='Fun', value="embed2", description='Fun command list', emoji=u'\U0001F389'),
			discord.SelectOption(label='Action', value="embed3", description='Info command list', emoji=u'\U0001F92A'),
			discord.SelectOption(label='Gifs', value="embed4", description='Gif command list', emoji=u'\U0001F92A'),
		]

		super().__init__(placeholder='Choose command category', min_values=1, max_values=1, options=options)

	async def callback(self, interaction: discord.Interaction):
		if interaction.user.id == self.id_:
			await interaction.response.edit_message(embed = help_embeds[self.values[0]])

class DropdownView(discord.ui.View):
	def __init__(self, id_:int):
		super().__init__()
		self.value = None

		self.add_item(Dropdown(id_))
		self.add_item(discord.ui.Button(label='Invite Eef!', url="https://discord.com/api/oauth2/authorize?client_id=815817857404502037&permissions=0&scope=bot%20applications.commands"))
		self.add_item(discord.ui.Button(label='Support server!', url="https://discord.gg/qUc3UJKpaz"))



@app_commands.command(name="help", description="Help command here to help!")
@app_commands.describe(
	command="The command to get more info about",
	ephemeral="To make the response only visible to you"
)
async def help_(interaction:discord.Interaction, command:str=None, ephemeral:bool=False):
	embed = discord.Embed(description='**Choose help category to learn more or use the command option to know more about a specific command**', color=0x80002f)
	await interaction.response.send_message(embed=embed, view=DropdownView(id_=interaction.user.id), ephemeral=ephemeral)


def get_command_name_list(interaction: discord.Interaction) -> List[str]:
	# [i for i in tree.get_commands() + tree.get_commands(guild=discord.Object(id=guild)) if isinstance(i, app_commands.Command)]
	name_list = []
	tree: discord.app_commands.CommandTree = interaction.client.tree
	for app_command in tree.get_commands() + tree.get_commands(guild=discord.Object(id=interaction.guild_id)):
		if isinstance(app_command, app_commands.Command):
			name_list.append(f"/{app_command.name}")
		elif isinstance(app_command, app_commands.Group):
			for i in app_command.commands:
				if isinstance(i, app_commands.Command):
					name_list.append(f"/{app_command.name}/{i.name}")

	return name_list 


def get_commands(interaction: discord.Interaction, current:str) -> List[str]:
	all_cmds = get_command_name_list(interaction)
	if not current: return sorted(all_cmds[:15])
	results = fuzzy_search(current, all_cmds)
	results = sorted(results[:15])
	return results 


@help_.autocomplete('command')
async def command_autocomplete(interaction: discord.Interaction,current: str,namespace: app_commands.Namespace) -> List[app_commands.Choice[str]]:
	results = get_commands(interaction, current)
	return [ app_commands.Choice(name=command, value=command) for command in results ]