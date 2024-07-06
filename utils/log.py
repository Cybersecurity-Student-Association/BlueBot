import discord
from variables.variables import log_channel

async def log(client: discord.Client, interaction: discord.Interaction, content):
    await client.get_channel(log_channel).send(content=content)

async def log(client: discord.client, content):
    await client.get_channel(log_channel).send(content=content)