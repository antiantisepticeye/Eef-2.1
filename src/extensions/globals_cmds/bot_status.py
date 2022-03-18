"""Imports"""

import platform
import discord
from discord import app_commands
from discord.http import Route
import psutil

def mem_info() -> str:
	v = psutil.virtual_memory()
	return f"{v.used//(1024*1024)}MiB / {v.total//(1024*1024)}MiB"

def os_info() -> str:
	return platform.system()


c = ''


def neofetch(interaction: discord.Interaction) -> str:
	ping_latency = round(interaction.client.latency * 1000)
	red = "[31m"
	pink = "[35m"
	white = "[37m"
	bold = "[1m"
	normal = "[0m"
	tx_color = "".join([ f"[{i}m███" for i in range(30, 38) ])
	bg_color = "".join([ f"[{i}m   " for i in range(40, 48) ])
	res = ""
	logo = f"""
cWMMMMMMMMMMMMMMMMMMMMMMk
KMMMMMMMMMMMMMMMMMMMMMMMM
 lWMMMMMMMMMMMMMMMMMMMMMM
  .OMMMMMMMMMNNNNNNNNNNNN
    ;NMMMMMMM0.          
      dMMMMMMMMo         
       .KMMMMMMMX,       
         WMMMMMMMM.      
       .KMMMMMMMX,       
      dMMMMMMMWo         
    ;NMMMMMMMO.          
  .OMMMMMMMMMNNNNNNNNNNNN
 lWMMMMMMMMMMMMMMMMMMMMMM
KMMMMMMMMMMMMMMMMMMMMMMMM
cWMMMMMMMMMMMMMMMMMMMMMMk"""
	info= f"""
{bold}{pink}	Eef{normal}{white}@{bold}{pink}Discord 
{normal}{white}-------------------
{bold}{pink}OS{normal}{white}: {os_info()}
{bold}{pink}Uptime{normal}{white}: {interaction.client.get_uptime()}
{bold}{pink}Memory{normal}{white}: {mem_info()}
{bold}{pink}Language{normal}{white}: Python 
{bold}{pink}API_BASE{normal}{white}: {Route.BASE.lstrip("https://discord.com")}
{bold}{pink}Latency{normal}{white}: {ping_latency} ms 




{tx_color}
{bg_color}


"""
	info = info.splitlines()[1:]
	logo = logo.splitlines()[1:]
	for i in range(15):
		idx = 24-int(6*i//4)
		logo_line = logo[i][:idx] + pink + logo[i][idx:]
		res += normal + red + "{0}\t\t{1}\n".format("".join(logo_line), info[i])

	return f"""```ansi
{res}
```"""



@app_commands.command(name="bot_status", description="Gets the status of the bot")
@app_commands.describe(
	ephemeral="To make the response only visible to you"
)
async def bot_status_(interaction: discord.Interaction, ephemeral: bool=False):
	embed = discord.Embed(color=0x80002f)
	embed.description = neofetch(interaction)
	await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
