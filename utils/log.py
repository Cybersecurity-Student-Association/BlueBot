import discord
from variables.variables import SERVER
from variables.channels import log_channel

async def log(client: discord.Client, content: str):
    await client.get_guild(SERVER).get_channel(log_channel).send(content=content, silent=True)