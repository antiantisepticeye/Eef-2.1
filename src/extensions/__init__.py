"""Imports"""
import discord


from .general import General
from .fun import Fun
from .info import Info
from .gifs import Gifs
from .image import Image
from .search import Search

from . import globals_cmds

def setup(tree: discord.app_commands.CommandTree):
	globals_cmds.setup(tree)
	tree.add_command(General, guild=discord.Object(id=573930213331697665))
	tree.add_command(Fun, guild=discord.Object(id=573930213331697665))
	tree.add_command(Info, guild=discord.Object(id=573930213331697665))
	tree.add_command(Gifs, guild=discord.Object(id=573930213331697665))
	tree.add_command(Image, guild=discord.Object(id=573930213331697665))
	tree.add_command(Search, guild=discord.Object(id=573930213331697665))