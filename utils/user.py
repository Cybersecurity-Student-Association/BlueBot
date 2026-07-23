import discord
from variables.variables import SERVER
def get_user_by_id(client: discord.Client, user_id: int):
    return client.get_guild(SERVER).get_member(user_id)

def get_user_by_name(client: discord.Client, username: str):
    return client.get_guild(SERVER).get_member_named(username)