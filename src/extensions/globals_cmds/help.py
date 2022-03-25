"""Imports"""

from pprint import pprint
import discord
from discord import app_commands


from typing import Dict, List, Optional, Tuple
from utils.fuzzy_search import fuzzy_search 
import discord


def get_cmd_groups(tree: discord.app_commands.CommandTree) -> List[discord.app_commands.Group]:
	if tree.client.debug_mode:
		cmd_groups = [ i for i in tree.get_commands(guild=tree.client.debug_guild, type=discord.AppCommandType.chat_input) if type(i) == discord.app_commands.Group ]
	else:
		cmd_groups = [ i for i in tree.get_commands(type=discord.AppCommandType.chat_input) if type(i) == discord.app_commands.Group ]
	return cmd_groups





class Dropdown(discord.ui.Select):
	def __init__(self, id_:int, cmd_groups):
		self.id_ = id_
		whitespace = " "
		self.help_embeds = [ 
	discord.Embed(title="Eef Hellp", description="```Use the`command` option to get more info on a specific command```", color=0x80002f)
	.add_field(name=f'{getattr(g, "emoji", "")} {g.name.title()} commands', value="__```" + "\n".join([ f"{i.name}{whitespace*(25-len(i.name))}{i.description}" for i in g.commands ]) + "```__")
	for g in cmd_groups ]
	
		options = [
			discord.SelectOption(label=g.name, value=str(i), description=f'{g.name.title()} command list', emoji=getattr(g, 'emoji', None))
			for i, g in enumerate(cmd_groups)
		]

		super().__init__(placeholder='Choose command category', min_values=1, max_values=1, options=options)

	async def callback(self, interaction: discord.Interaction):
		if interaction.user.id == self.id_:
			await interaction.response.edit_message(embed = self.help_embeds[int(self.values[0])])

class DropdownView(discord.ui.View):
	def __init__(self, id_:int, cmd_groups):
		super().__init__()
		self.value = None

		self.add_item(Dropdown(id_, cmd_groups))
		self.add_item(discord.ui.Button(label='Invite Eef!', url="https://discord.com/api/oauth2/authorize?client_id=815817857404502037&permissions=0&scope=bot%20applications.commands"))
		self.add_item(discord.ui.Button(label='Support server!', url="https://discord.gg/qUc3UJKpaz"))


def find_command(command_name: str, interaction: discord.Interaction) -> Optional[discord.app_commands.Command]:
	found_command = None
	tree: discord.app_commands.CommandTree = interaction.client.tree
	for app_command in tree.get_commands() + tree.get_commands(guild=discord.Object(id=interaction.guild_id)):
		if isinstance(app_command, app_commands.Command) and app_command.name == command_name:
			if command_name == app_command.name:
				found_command = app_command
		elif isinstance(app_command, app_commands.Group):
			for i in app_command.commands:
				if isinstance(i, app_commands.Command) and i.name == command_name:
					found_command = i
	return found_command

@app_commands.command(name="help", description="Help command here to help!")
@app_commands.describe(
	command="The command to get more info about",
	ephemeral="To make the response only visible to you"
)
async def help_(interaction:discord.Interaction, command:str=None, ephemeral:bool=False):
	
	if not command:
		embed = discord.Embed(description='**Choose help category to learn more or use the command option to know more about a specific command**', color=0x80002f)
		await interaction.response.send_message(embed=embed, view=DropdownView(id_=interaction.user.id, cmd_groups=get_cmd_groups(interaction.client.tree)), ephemeral=ephemeral)
	else:
		found_command = find_command(command, interaction)
		if found_command == None: return await interaction.client.send_error(interaction, "Command Not Found", ephemeral=ephemeral)
		else:
			embed = discord.Embed(title=found_command.name.title(), color=0x80002f)
			embed.set_author(name ="Eef Hellp")
			embed.add_field(name = "Description", value= found_command.description, inline=False)
			w = " "
			params = '\n\n'.join([ i.name + w*(15-len(i.name)) + i.description for i in found_command._params.values() ])
			embed.add_field(name = "Options", value=f"```{params}```", inline=False)
						
			await interaction.response.send_message(embed=embed, ephemeral=ephemeral)




def get_command_name_list(interaction: discord.Interaction) -> Dict[str, str]:
	name_list = []
	tree: discord.app_commands.CommandTree = interaction.client.tree
	for app_command in tree.get_commands() + tree.get_commands(guild=discord.Object(id=interaction.guild_id)):
		if isinstance(app_command, app_commands.Command):
			name_list.append((f"/{app_command.name}", app_command.name))
		elif isinstance(app_command, app_commands.Group):
			for i in app_command.commands:
				if isinstance(i, app_commands.Command):
					name_list.append((f"/{app_command.name}/{i.name}", i.name))

	return {i[0]:i[1] for i in name_list} 


def get_commands(interaction: discord.Interaction, current:str) -> Dict[str, str]:
	d = get_command_name_list(interaction)
	all_cmds = list(d.keys())
	if not current: return { i: d[i] for i in sorted(all_cmds[:15]) }
	results = fuzzy_search(current, all_cmds)
	results = sorted(results[:15])
	return { i: d[i] for i in results } 


@help_.autocomplete('command')
async def command_autocomplete(interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
	results = get_commands(interaction, current)
	return [ app_commands.Choice(name=command[0], value=command[1]) for command in results.items() ][:7]