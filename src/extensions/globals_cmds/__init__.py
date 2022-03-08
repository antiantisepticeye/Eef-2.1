"""Imports"""

from discord import app_commands
import discord


"""Command Imports"""

from . import (
	ping,
	help
	
)


def setup(tree: app_commands.CommandTree):
	tree.add_command(ping.ping_, guild=discord.Object(id=573930213331697665))
	tree.add_command(help.help_, guild=discord.Object(id=573930213331697665))