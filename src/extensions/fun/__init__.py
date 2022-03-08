"""imports"""

import discord
from discord import app_commands

"""Command Imports"""
from .cat import cat_
from .dog import dog_
from .choose import choose_
from .rip import rip_


Fun = app_commands.Group(name="fun", description="Fun commands!")
Fun.add_command(cat_)
Fun.add_command(dog_)
Fun.add_command(choose_)
Fun.add_command(rip_)
