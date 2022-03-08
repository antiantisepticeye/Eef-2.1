"""imports"""

import discord
from discord import app_commands

"""Command Imports"""
from .avatar import avatar_


General = app_commands.Group(name="general", description="General commands!")
General.add_command(avatar_)

