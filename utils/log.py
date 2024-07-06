import discord
from variables.variables import log_channel

async def log(client: discord.Client, content: str):
    await client.get_channel(log_channel).send(content=content)