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
	tree.add_command(General)
	tree.add_command(Fun)
	tree.add_command(Info)
	tree.add_command(Gifs)
	tree.add_command(Image)
	tree.add_command(Search)