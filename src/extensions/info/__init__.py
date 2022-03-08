"""imports"""

import discord
from discord import app_commands

"""Command Imports"""

from .user import user_
from .role import role_
from .server import server_
from .emoji import emoji_


Info = app_commands.Group(name="info", description="Info commands!")
Info.add_command(user_)
Info.add_command(role_)
Info.add_command(server_)
Info.add_command(emoji_)
