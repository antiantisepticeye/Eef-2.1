"""Imports"""

from discord import app_commands
import discord


"""Command Imports"""

from . import (
	ping,
	help
	
)


def setup(tree: app_commands.CommandTree, guild=None):
	if guild:
		tree.add_command(ping.ping_, guild=guild)
		tree.add_command(help.help_, guild=guild)
	else:
		tree.add_command(ping.ping_)
		tree.add_command(help.help_)