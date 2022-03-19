"""Imports"""

from math import floor
import os
from asyncio import sleep
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()
from pprint import pprint


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


def get_uptime() -> str:
	current_date = datetime.now()
	delta: timedelta = current_date - client.start_date
	total_seconds = delta.seconds
	total_minutes = floor(total_seconds/(60**1))
	total_hours = floor(total_seconds/(60**2))
	total_days = floor(total_seconds/(60**2 * 24))
	d = {
		"days": total_days % 30,
		"hours": total_hours % 24,
		"minutes": total_minutes % 60
	}
	return ", ".join([f"{v} {k}" for k,v in d.items() if v]) or str(floor(total_seconds)) + " seconds"


"""Add variables to the client object"""
client.tree = tree
client.send_error = send_error_embed
client.API_BASE = "https://api.eefbot.ga"
client.API_TOKEN = os.getenv("API_TOKEN")
client.debug_guild = discord.Object(id=int(os.getenv('DEBUG_GUILD'))) if os.getenv('DEBUG_GUILD') else None
client.debug_mode = bool(client.debug_guild)
client.start_date = datetime.now()
client.get_uptime = get_uptime


@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game("Eef v2.1 | /help | Now using slash commands!"))	
	print("Syncing commands...")
	if client.debug_mode:
		await tree.sync(guild=client.debug_guild)
	else: 
		await tree.sync()
	print("Bot is ready!")
	

setup(tree)



client.run(os.getenv('BOT_TOKEN'))