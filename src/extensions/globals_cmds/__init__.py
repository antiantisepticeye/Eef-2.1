"""Imports"""

from discord import app_commands
import discord


"""Command Imports"""

from . import (
	bot_status,
	ping,
	help
	
)


def setup(tree: app_commands.CommandTree, guild=None):
	if guild:
		tree.add_command(ping.ping_, guild=guild)
		tree.add_command(help.help_, guild=guild)
		tree.add_command(bot_status.bot_status_, guild=guild)
	else:
		tree.add_command(ping.ping_)
		tree.add_command(help.help_)
		tree.add_command(bot_status.bot_status_, guild=guild)