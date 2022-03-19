"""imports"""

import discord
from discord import app_commands

"""Command Imports"""
from .hug import hug_
from .bonk import bonk_
from .kick import kick_
from .pat import pat_
from .poke import poke_
from .slap import slap_



Gifs = app_commands.Group(name="gifs", description="gif commands!")
setattr(Gifs, "emoji", "💃")
Gifs.add_command(hug_)
Gifs.add_command(bonk_)
Gifs.add_command(kick_)
Gifs.add_command(pat_)
Gifs.add_command(poke_)
Gifs.add_command(slap_)

