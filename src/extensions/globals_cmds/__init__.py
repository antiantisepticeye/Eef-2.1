"""Imports"""

from discord import app_commands
import discord


"""Command Imports"""

from . import (
	ping,
	help
	
)


def setup(tree: app_commands.CommandTree):
	tree.add_command(ping.ping_)
	tree.add_command(help.help_)