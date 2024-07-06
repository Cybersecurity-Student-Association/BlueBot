import discord

async def get_user_by_id(client: discord.Client, guild_id: int, user_id: int):
    return client.get_guild(guild_id).get_member(user_id)