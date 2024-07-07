import discord
from variables.variables import SERVER

def get_channel_by_name(client: discord.Client, target_name: str):
    for channel in client.get_all_channels():
        if channel.name == target_name and channel.guild.id == SERVER:
            return channel
