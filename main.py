import discord
from discord.ext import commands
import music

cogs = [music]
description = 'A music playing bot'

client = commands.Bot(command_prefix='.', description=description, intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("bot token")

