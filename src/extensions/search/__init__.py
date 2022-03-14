"""imports"""

import discord
from discord import app_commands

"""Command Imports"""


from .youtube import youtube_


Search = app_commands.Group(name="search", description="Search commands!")
Search.add_command(youtube_)