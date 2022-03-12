"""Imports"""

import os
from asyncio import sleep
from dotenv import load_dotenv
load_dotenv()

"""Discord Imports"""

import discord
from discord import app_commands

from error_handler import send_error_embed

""" Import Commands """

from extensions import setup


"""Initialization"""

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

"""Add variables to the client object"""
client.tree = tree
client.send_error = send_error_embed
client.API_URL = "https://api.eefbot.ga"


@client.event
async def on_ready():
	print("Syncing commands...")
	await tree.sync(guild=discord.Object(id=573930213331697665))
	print("Bot is ready!")


setup(tree)

client.run(os.getenv('BOT_TOKEN'))