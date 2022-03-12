"""imports"""

import discord
from discord import app_commands

"""Command Imports"""
from .avatar import avatar_
from .server_icon import server_icon_
from .server_banner import server_banner_


General = app_commands.Group(name="general", description="General commands!")
General.add_command(avatar_)
General.add_command(server_icon_)
General.add_command(server_banner_)

