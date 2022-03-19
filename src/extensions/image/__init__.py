"""imports"""

import discord
from discord import app_commands

"""Command Imports"""

from .wasted import wasted_
from .wanted import wanted_
from .chromatic import chromatic_
from .legofy import legofy_


Image = app_commands.Group(name="image", description="Image commands!")
setattr(Image, "emoji", "📷")
Image.add_command(wasted_)
Image.add_command(wanted_)
Image.add_command(chromatic_)
Image.add_command(legofy_)
