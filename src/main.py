"""Imports"""

from math import floor
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()


"""Discord Imports"""

import discord
from discord import app_commands


"""Import Commands"""

from extensions import setup

"""Other Import"""

from utils.parse_delta import parse_delta


"""Initialization"""

intents = discord.Intents.default()
intents.message_content = True


class EefClient(discord.Client):
	
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.tree = app_commands.CommandTree(self)
		self.API_BASE = "https://api.eefbot.ga"
		self.API_TOKEN = os.getenv("API_TOKEN")
		self.debug_guild = discord.Object(id=int(os.getenv('DEBUG_GUILD'))) if os.getenv('DEBUG_GUILD') else None
		self.debug_mode = bool(self.debug_guild)
		self.start_date = datetime.fromtimestamp(1647739935)
		self.event(self.on_ready)
	
	
	"""Error Handler method to send an error embed if needed."""

	@classmethod
	async def send_error(cls, interaction:discord.Interaction, error_message:str, webhook: discord.Webhook=None, ephemeral=True) -> None:
		embed = discord.Embed(description=f'**{error_message}**', color=0x80002f)
		if not webhook:
			await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
		else:
			await webhook.send(embed=embed, ephemeral=ephemeral)


	"""A method for the ready event, fires when the client gets ready"""
	
	async def on_ready(self):
		await client.change_presence(activity=discord.Game("Eef v2.1 | /help | Now using slash commands!"))	
		print("Syncing commands...")

		if self.debug_mode:
			await self.tree.sync(guild=self.debug_guild)
		
		await self.tree.sync()
		print("Bot is ready!")


	"""A method to get the uptime of the bot as a string  (for getting bot status)"""

	def get_uptime(self) -> str:
		current_date = datetime.now()
		delta: timedelta = current_date - self.start_date
		return parse_delta(delta)
	

client = EefClient(intents=intents)


setup(client.tree)


client.run(os.getenv('BOT_TOKEN'))